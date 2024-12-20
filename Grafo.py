from Nodo import Nodo  # Importa la clase Nodo para representar los nodos del grafo
from Arista import Arista  # Importa la clase Arista para representar las conexiones entre nodos
import queue, re, copy
import pygame, random, math
class Grafo:
    def __init__(self, id="grafo"):
        # Inicializa un grafo con un identificador (id), y opciones para ser dirigido o tener aristas auto-conectadas.
        self.id = id  # Identificador del grafo
        self.nodos = {}  # Diccionario para almacenar los nodos del grafo
        self.aristas = {}  # Diccionario para almacenar las aristas del grafo

    def agregar_nodo(self, id):
        # Crea un nuevo nodo y lo agrega al diccionario de nodos.
        nuevo_nodo = Nodo(id)  # Crea una instancia de Nodo
        self.nodos[nuevo_nodo.id] = nuevo_nodo  # Almacena el nodo en el diccionario

    def agregar_arista(self, n1, n2):
        # Crea una nueva arista entre dos nodos y actualiza sus grados.
        nueva_arista = Arista(self.nodos[n1], self.nodos[n2])  # Crea una instancia de Arista
        self.aristas[nueva_arista.id] = nueva_arista  # Almacena la arista en el diccionario
        self.nodos[n1].grado += 1  # Incrementa el grado del nodo n1
        self.nodos[n2].grado += 1  # Incrementa el grado del nodo n2

    def grado(self, nodo):
        # Retorna el grado del nodo especificado.
        return self.nodos[nodo].grado  # Devuelve el grado del nodo

    def total_aristas(self):
        # Retorna el número total de aristas en el grafo.
        return len(self.aristas)  # Devuelve la cantidad de aristas

    def repetida(self, ni, nf, pesos=False, valor=False):
        # Verifica si existe una arista entre dos nodos (ni y nf) en cualquier dirección.
        arista1 = Arista(self.nodos[ni], self.nodos[nf])  # Crea una arista de ni a nf
        arista2 = Arista(self.nodos[nf], self.nodos[ni])  # Crea una arista de nf a ni
        
       
        # Comprueba si alguna de las aristas ya está en el diccionario de aristas
        if arista1.id in self.aristas:
            if pesos:
                return self.aristas[arista1.id].peso
            if valor:
                return self.aristas[arista1.id]
            return True
        if arista2.id in self.aristas:
            if pesos:
                return self.aristas[arista2.id].peso
            if valor:
                return self.aristas[arista2.id]
            return True
        return False
    def graficar(self,etiqueta=False,s=None):
        # Genera un archivo Graphviz para visualizar el grafo.
        contenido = ''
        contenido += 'digraph ' + self.id + ' {\n'  # Comienza la declaración del grafo en formato DOT
        if(etiqueta==True):
            for llave, arista in self.aristas.items():  # Itera sobre las aristas para imprimirlas
                if(s==None):
                    contenido+=arista.id +' [label = '+str(arista.peso)+'];\n'
                else:
                    contenido+= '\"'+str(arista.n1.id)+'-'+str(self.nodos[s].id) +'= '+str(arista.n1.distancia)+'\" - '+'\"'+str(arista.n2.id)+'-'+str(self.nodos[s].id) +'= '+str(arista.n2.distancia)+'\" [label = '+str(arista.peso)+'];\n'

        else:
            for llave, nodo in self.nodos.items():  # Itera sobre los nodos para imprimirlos
                contenido += str(llave) + ';\n'  # Agrega cada nodo al contenido

            for llave, arista in self.aristas.items():  # Itera sobre las aristas para imprimirlas
                contenido += arista.id + ';\n'  # Agrega cada arista al contenido

        contenido += '}'  # Cierra la declaración del grafo

        nombre_completo =self.id +'.gv'  # Define el nombre del archivo de salida
        f = open(nombre_completo, "w")  # Abre el archivo para escritura
        f.write(contenido)  # Escribe el contenido en el archivo
        f.close()  # Cierra el archivo
        print('Archivo Graphviz generado: ' + nombre_completo + '\n')  # Imprime un mensaje de confirmación

    #Proyecto 2
    def cargar_grafo(self, archivo):
        with open(archivo, "r") as file:
            contenido = file.readlines()
        for linea in contenido:
            linea = linea.strip()
            # Saltar líneas de comentarios y apertura/cierre de grafo
            if linea.startswith("digraph") or linea == "{" or linea == "}":
                continue

            # Verificar si es un nodo (formato nodo;)
            if ";" in linea and "-" not in linea:
                nodo = linea.replace(";", "")
                self.agregar_nodo(int(nodo))

            # Verificar si es una arista (formato nodo1 -> nodo2;)
            elif "-" in linea:
                match = re.match(r"(\w+)\s*-\s*(\w+);", linea)
                if match:
                    n1, n2 = match.groups()
                    self.agregar_arista(int(n1),int(n2))

        print("Grafo cargado desde el archivo:", archivo)

    def totalNodos(self):
        # Devuelve el número total de nodos en el grafo
        return len(self.nodos)

    def nodosConectados(self,nodo):
        nodos_conectados=[]
        for key, value in self.aristas.items():
            if(value.n1 == self.nodos[nodo]):
                nodos_conectados.append(int(str(value.n2)))
            if(value.n2==self.nodos[nodo]):
                nodos_conectados.append(int(str(value.n1)))
        return nodos_conectados

    def DFS_iterativo(self, s):
        # Implementación iterativa de la búsqueda en profundidad (DFS) en un grafo.
        nombre ='Arboles_GV/DFS Iterativo ' + self.id + ' raiz = '+ str(s) # Nombre del nuevo grafo que representará el árbol DFS
        obj = Grafo(nombre)  # Grafo que almacenará el resultado del árbol DFS
        nodo_recorrido = ["no"] * (self.totalNodos())  # Lista para registrar los nodos visitados
        pila = [s]  # Pila para gestionar el orden de los nodos a explorar en DFS
        nodo_recorrido[s] = "si"  # Marcamos el nodo de inicio como visitado
        obj.agregar_nodo(s)  # Agregamos el nodo inicial al árbol DFS
        while pila:
            s = pila.pop()  # Extraemos el último nodo agregado (LIFO) de la pila
            vecinos = self.nodosConectados(s)  # Obtenemos los nodos vecinos
            for vecino in vecinos:
                if nodo_recorrido[vecino] == "no":  # Si el vecino no ha sido visitado
                    pila.append(vecino)  # Lo agregamos a la pila para continuar con la exploración
                    nodo_recorrido[vecino] = "si"  # Marcamos el vecino como visitado
                    obj.agregar_nodo(vecino)  # Agregamos el vecino al árbol DFS
                    obj.agregar_arista(s,vecino)# Agregamos arista al árbol
        return obj  # Retornamos el árbol DFS

    def DFS_recursivo(self, s):
        # Implementación recursiva de DFS en un grafo.
        nombre = 'Arboles_GV/DFS Recursivo '  + self.id + ' raiz = '+ str(s)  # Nombre del nuevo grafo que representará el árbol DFS
        obj = Grafo(nombre)  # Grafo que almacenará el resultado del árbol DFS
        nodo_recorrido = ["no"] * (self.totalNodos())  # Lista para registrar los nodos visitados

        def dfs_aux(s):
            # Función auxiliar que realiza DFS de manera recursiva
            nodo_recorrido[s] = "si"  # Marcamos el nodo como visitado
           
            vecinos = self.nodosConectados(s)  # Obtenemos los vecinos del nodo actual
            for vecino in vecinos:
                if nodo_recorrido[vecino] == "no":  # Si el vecino no ha sido visitado
                    obj.agregar_nodo(vecino)
                    obj.agregar_arista(s,vecino)  # Agregamos la arista en el árbol DFS
                    dfs_aux(vecino)  # Llamada recursiva para explorar el vecino
        obj.agregar_nodo(s)  # Agregamos el nodo al árbol DFS
        dfs_aux(s)  # Comenzamos la búsqueda en profundidad desde el nodo `s`
        return obj  # Retornamos el árbol DFS

    def BFS(self, s):
        # Implementación de un árbol BFS (búsqueda en amplitud) en un grafo.
        nombre = 'Arboles_GV/BFS ' +  self.id + ' raiz = '+ str(s) # Nombre del nuevo grafo que representará el árbol BFS
        obj = Grafo(nombre)  # Grafo que almacenará el resultado del árbol BFS
        nodo_recorrido = ["no"] * (self.totalNodos())  # Lista para registrar los nodos visitados
        cola = [s]  # Cola para gestionar el orden de los nodos a explorar en BFS
        nodo_recorrido[s] = "si"  # Marcamos el nodo de inicio como visitado
        obj.agregar_nodo(s)  # Agregamos el nodo inicial al árbol BFS

        while cola:
            s = cola.pop(0)  # Extraemos el primer nodo de la cola (FIFO)
            vecinos = self.nodosConectados(s)  # Obtenemos los nodos vecinos

            for vecino in vecinos:
                if nodo_recorrido[vecino] == "no":  # Si el vecino no ha sido visitado
                    cola.append(vecino)  # Lo agregamos a la cola para continuar con la exploración
                    nodo_recorrido[vecino] = "si"  # Marcamos el vecino como visitado
                    obj.agregar_nodo(vecino)  # Agregamos el vecino al árbol BFS
                    obj.agregar_arista(s, vecino)  # Conectamos el nodo actual con su vecino en el árbol BFS

        return obj  # Retornamos el árbol BFS

    #Proyecto 3

    def Dijkstra(self, s):
        # Definir el nombre del nuevo grafo que representará el algoritmo Dijkstra
        nombre = 'Dijkstra_GV/Dijkstra_' +  self.id + ' raiz = ' + str(s)
        # Crear el objeto grafo
        obj = Grafo(nombre)
        
        # Crear cola de prioridad para la implementación de Dijkstra
        cola_prioridad = queue.PriorityQueue()
        
        # Inicializar una lista para marcar los nodos recorridos
        nodo_recorrido = ["no"] * (self.totalNodos())
        
        # Establecer la distancia del nodo fuente a 0
        self.nodos[s].distancia = 0
        # Agregar el nodo fuente a la cola de prioridad
        cola_prioridad.put(self.nodos[s])
        
        # Ejecutar el algoritmo mientras haya nodos en la cola de prioridad
        while not cola_prioridad.empty():
            # Extraer el nodo con la menor distancia (esto es el nodo "s")
            s = cola_prioridad.get()  # Extrae la tupla, por lo que solo se obtiene el nodo
            nodo_recorrido[s.id] = "si"  # Marcar el nodo como visitado
            
            # Obtener los nodos vecinos del nodo actual
            vecinos = self.nodosConectados(s.id)
            
            for vecino in vecinos:
                if nodo_recorrido[vecino] == "no":  # Si el vecino no ha sido visitado
                    # Obtener el peso de la arista entre el nodo y su vecino
                    peso_arista = self.repetida(s.id, vecino, pesos=True)
                    
                    # Si el vecino puede ser actualizado con una mejor distancia
                    if self.nodos[vecino].distancia > s.distancia + peso_arista:
                        self.nodos[vecino].distancia = s.distancia + peso_arista
                        self.nodos[vecino].padre = s.id
                        # Agregar el vecino a la cola de prioridad para continuar el recorrido
                        cola_prioridad.put(self.nodos[vecino])
        
        # Después de ejecutar Dijkstra, agregar los nodos y aristas al grafo resultante
        for llave, nodo in self.nodos.items():
            obj.agregar_nodo(nodo.id)  # Agregar el nodo al nuevo grafo
            if nodo.padre is not None:
                # Si el nodo tiene un padre, agregar la arista correspondiente al nuevo grafo
                arista_aux = self.repetida(nodo.id, nodo.padre, valor=True)
                if arista_aux:  # Si existe la arista en el grafo original
                    obj.aristas[arista_aux.id] = arista_aux  # Agregar la arista al grafo Dijkstra
        
        return obj
    
    #Proyecto 4
    def encontrar_conjunto(self, nodo):
        # Método de "find" para encontrar el conjunto al que pertenece un nodo
        if self.conjunto[nodo] == nodo:
            return nodo
        return self.encontrar_conjunto(self.conjunto[nodo])
    
    def Kruskal(self):
        # Definir el nombre del nuevo grafo que representará el algoritmo de Kruskal
        nombre = 'Voraces_GV/Kruskal_' + self.id
        obj = Grafo(nombre)
        
        # Crear cola de prioridad para las aristas
        cola_prioridad = queue.PriorityQueue()
    
        # Inicializar las estructuras para los conjuntos disjuntos
        self.conjunto = [None] * (self.totalNodos())
        obj.nodos=self.nodos.copy()
        # Inicializar los nodos en el grafo
        for llave, nodo in self.nodos.items():
            self.conjunto[nodo.id] = nodo.id  # Inicializar el conjunto de cada nodo
    
        # Agregar todas las aristas a la cola de prioridad
        for llave, arista in self.aristas.items():
            cola_prioridad.put(self.aristas[llave])
        
        mst_costo = 0  # Variable para almacenar el costo total del MST (Árbol de expansión mínimo)
        
        # Ejecutar Kruskal mientras haya aristas en la cola de prioridad
        while not cola_prioridad.empty():
            # Extraer la siguiente arista de menor peso
            s = cola_prioridad.get()
            conjunto1 = self.encontrar_conjunto(s.n1.id)
            conjunto2 = self.encontrar_conjunto(s.n2.id)
    
            # Si los nodos no están en el mismo conjunto, añadir la arista al MST
            if conjunto1 != conjunto2:
                arista_aux = self.repetida(s.n1.id, s.n2.id, valor=True)
                obj.aristas[arista_aux.id] = arista_aux
                mst_costo += s.peso  # Sumar el peso de la arista al costo del MST
                
                # Unir los conjuntos
                if self.nodos[conjunto1].grado < self.nodos[conjunto2].grado:
                    self.conjunto[conjunto1] = conjunto2
                    self.nodos[conjunto2].grado += 1
                else:
                    self.conjunto[conjunto2] = conjunto1
                    self.nodos[conjunto1].grado += 1
    
        # Mostrar el costo del MST y devolver el grafo resultante
        print(nombre,'- MST costo:', mst_costo)
        return obj
    
    def Kruskal_inverso(self):
        # Definir el nombre del grafo para Kruskal inverso
        nombre = 'Voraces_GV/Kruskal_Inverso_' + self.id
        obj = copy.deepcopy(self)  # Crear una copia profunda del grafo original
        obj.id = nombre
        cola_prioridad = queue.PriorityQueue()  # Crear una cola de prioridad
        mst_costo = 0  # Inicializar el costo del MST
    
        # Agregar todas las aristas con pesos negativos para invertir la cola de prioridad
        for llave, arista in self.aristas.items():
            cola_prioridad.put((-arista.peso, llave))  # Invertir el peso de la arista
    
        # Obtener el total de nodos
        totalNodos = obj.totalNodos()
    
        # Ejecutar el algoritmo mientras haya aristas en la cola de prioridad
        while not cola_prioridad.empty():
            peso, arista = cola_prioridad.get()  # Extraer la arista con el menor peso
            del obj.aristas[arista]  # Eliminar la arista del grafo
            
            # Verificar si el grafo se desconecta al eliminar la arista
            objDFS = obj.DFS_recursivo(1)  # Realizar un DFS para comprobar la conexión
            totalNodosDFS = objDFS.totalNodos()
    
            # Si el grafo se desconecta, volver a agregar la arista
            if totalNodosDFS < totalNodos:
                obj.aristas[arista] = self.aristas[arista]
                mst_costo += peso  # Sumar el costo de la arista al MST
    
        mst_costo *= -1  # Convertir el costo negativo a positivo
        print(nombre, '- MST costo:', mst_costo)  # Imprimir el costo del MST
        return obj  # Devolver el grafo modificado
    
    def Prim(self, s):
        # Definir el nombre del nuevo grafo que representará el algoritmo de Prim
        nombre = 'Voraces_GV/Prim_' + self.id
        obj = Grafo(nombre)  # Crear un nuevo grafo para el MST
        mst_costo = 0  # Inicializar el costo del MST
        nodo_recorrido = ["no"] * (self.totalNodos())  # Marcar los nodos como no visitados
        key = [float('inf')] * (self.totalNodos())  # Inicializar las claves de los nodos
    
        # Crear cola de prioridad para Prim
        cola_prioridad = queue.PriorityQueue()
        cola_prioridad.put((0, s))  # Agregar el nodo inicial con distancia 0
    
        # Ejecutar Prim mientras haya nodos en la cola de prioridad
        while not cola_prioridad.empty():
            peso, nodo = cola_prioridad.get()  # Extraer el nodo con el menor peso
            if nodo_recorrido[nodo] == "si":  # Si el nodo ya ha sido visitado, omitirlo
                continue
            mst_costo += peso  # Sumar el peso de la arista al MST
            nodo_recorrido[nodo] = "si"  # Marcar el nodo como visitado
            
            # Obtener los vecinos del nodo
            vecinos = self.nodosConectados(nodo)
            
            for vecino in vecinos:
                peso_arista = self.repetida(nodo, vecino, pesos=True)  # Obtener el peso de la arista
                if nodo_recorrido[vecino] == "no" and key[vecino] > peso_arista:
                    cola_prioridad.put((peso_arista, vecino))  # Agregar vecino a la cola de prioridad
                    key[vecino] = peso_arista  # Actualizar la clave del vecino
                    self.nodos[vecino].padre = nodo  # Establecer el nodo padre
    
        # Después de ejecutar Prim, agregar los nodos y aristas al grafo resultante
        for llave, nodo in self.nodos.items():
            obj.agregar_nodo(nodo.id)  # Agregar los nodos al nuevo grafo
            if nodo.padre is not None:
                arista_aux = self.repetida(nodo.id, nodo.padre, valor=True)  # Obtener la arista
                if arista_aux:
                    obj.aristas[arista_aux.id] = arista_aux  # Agregar la arista al grafo
    
        # Mostrar el costo del MST y devolver el grafo resultante
        print(nombre, 'MST costo:', mst_costo)  # Imprimir el costo del MST
        return obj  # Devolver el grafo modificado


    def Calcular_fuerzas(self, k_repulsion, k_atraccion, iteracciones, k, max_velocidad, umbral_distancia):
        WHITE = (255, 255, 255)  # Color blanco para el fondo
        BLACK = (0, 0, 0)  # Color negro para los elementos
        RED = (255, 0, 0)  # Color rojo para los nodos
        BLUE = (0, 0, 255)  # Color azul para las aristas
        WIDTH, HEIGHT = 1100, 750  # Dimensiones de la ventana de pygame

        # Inicializa pygame
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Crear la pantalla de visualización
        pygame.display.set_caption("Dibujo de un grafo")  # Título de la ventana

        def dibujar():
            screen.fill(WHITE)  # Llenar el fondo con color blanco
            for llave, nodo in self.nodos.items():
                pygame.draw.circle(screen, RED, nodo.coordenadas, 8)  # Dibujar los nodos
            # Dibujar aristas (conexiones entre los nodos)
            for llave, arista in self.aristas.items():
                pygame.draw.line(screen, BLUE, arista.n1.coordenadas, arista.n2.coordenadas, 1)  # Dibujar aristas

            pygame.display.flip()  # Actualizar la pantalla
            clock.tick(10000)  # Establecer el límite de la tasa de cuadros por segundo

        # Bucle principal
        running = True
        clock = pygame.time.Clock()  # Inicializar el reloj de pygame
        for _ in range(iteracciones):  # Realizar las iteracciones especificadas

            for llave, nodo in self.nodos.items():
                nodo.fuerzas[0] = 0.0  # Inicializar las fuerzas del nodo
                nodo.fuerzas[1] = 0.0
            
            for llave1, nodo1 in self.nodos.items():
                # Fuerzas de repulsión entre todos los nodos
                for llave2, nodo2 in self.nodos.items():
                    if nodo1 != nodo2:  # Evitar la fuerza entre un nodo y él mismo
                        difx = nodo1.coordenadas[0] - nodo2.coordenadas[0]  # Diferencia en el eje x
                        dify = nodo1.coordenadas[1] - nodo2.coordenadas[1]  # Diferencia en el eje y
                        distancia = math.sqrt(difx ** 2 + dify ** 2) or 1  # Calcular la distancia entre los nodos

                        # Si la distancia es menor que el umbral, no se aplica fuerza de repulsión
                        if distancia > umbral_distancia:
                            fuerza_repulsion = k_repulsion / distancia  # Ley de Coulomb
                            nodo1.fuerzas[0] += fuerza_repulsion * difx / distancia
                            nodo1.fuerzas[1] += fuerza_repulsion * dify / distancia

            # Fuerzas de atracción por cada arista
            for llave, arista in self.aristas.items():
                difx = arista.n1.coordenadas[0] - arista.n2.coordenadas[0]  # Diferencia en el eje x
                dify = arista.n1.coordenadas[1] - arista.n2.coordenadas[1]  # Diferencia en el eje y
                distancia = math.sqrt(difx ** 2 + dify ** 2) or 1  # Calcular la distancia entre los nodos de la arista
                # Si la distancia es menor que el umbral, no se aplica fuerza de atracción
                if distancia > umbral_distancia:
                    fuerza_atraccion = -k_atraccion * math.log(distancia)  # Cálculo de la fuerza de atracción
                    arista.n1.fuerzas[0] += fuerza_atraccion * difx / distancia
                    arista.n1.fuerzas[1] += fuerza_atraccion * dify / distancia
                    arista.n2.fuerzas[0] -= fuerza_atraccion * difx / distancia
                    arista.n2.fuerzas[1] -= fuerza_atraccion * dify / distancia

            # Actualizar posiciones de los nodos
            for llave, nodo in self.nodos.items():
                nodo.fuerza[0] = max(-max_velocidad, min(max_velocidad, (nodo.fuerza[0] + nodo.fuerzas[0]) * k))
                nodo.fuerza[1] = max(-max_velocidad, min(max_velocidad, (nodo.fuerza[1] + nodo.fuerzas[1]) * k))
                nodo.coordenadas[0] += nodo.fuerza[0]  # Actualizar la posición del nodo en el eje x
                nodo.coordenadas[1] += nodo.fuerza[1]  # Actualizar la posición del nodo en el eje y

            dibujar()  # Llamar a la función de dibujo para mostrar el grafo

        # Esperar hasta que el usuario cierre la ventana
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()  # Cerrar pygame