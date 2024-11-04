from Nodo import Nodo  # Importa la clase Nodo para representar los nodos del grafo
from Arista import Arista  # Importa la clase Arista para representar las conexiones entre nodos
import re
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

    def repetida(self, ni, nf):
        # Verifica si existe una arista entre dos nodos (ni y nf) en cualquier dirección.
        arista1 = Arista(self.nodos[ni], self.nodos[nf])  # Crea una arista de ni a nf
        arista2 = Arista(self.nodos[nf], self.nodos[ni])  # Crea una arista de nf a ni
        # Comprueba si alguna de las aristas ya está en el diccionario de aristas
        if (arista1.id in self.aristas) or (arista2.id in self.aristas):
            return True  # Retorna True si la arista es repetida

    def graficar(self):
        # Genera un archivo Graphviz para visualizar el grafo.
        contenido = ''
        contenido += 'digraph ' + self.id + ' {\n'  # Comienza la declaración del grafo en formato DOT

        for nodo in self.nodos:  # Itera sobre los nodos para imprimirlos
            contenido += str(nodo) + ';\n'  # Agrega cada nodo al contenido

        for key, value in self.aristas.items():  # Itera sobre las aristas para imprimirlas
            contenido += value.id + ';\n'  # Agrega cada arista al contenido

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
        nombre ='Arboles_GV/DFS_ITERATIVO_' + self.id + 'raiz = '+ str(s) # Nombre del nuevo grafo que representará el árbol DFS
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
        nombre = 'Arboles_GV/DFS_RECURSIVO_'  + self.id + 'raiz = '+ str(s)  # Nombre del nuevo grafo que representará el árbol DFS
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
        nombre = 'Arboles_GV/BFS_' +  self.id + 'raiz = '+ str(s) # Nombre del nuevo grafo que representará el árbol BFS
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



