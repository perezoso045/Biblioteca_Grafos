from Nodo import Nodo  # Importa la clase Nodo para representar los nodos del grafo
from Arista import Arista  # Importa la clase Arista para representar las conexiones entre nodos

class Grafo:
    def __init__(self, id="grafo", dirigido=False, auto=False):
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

        nombre_completo = self.id + '.gv'  # Define el nombre del archivo de salida
        f = open(nombre_completo, "w")  # Abre el archivo para escritura
        f.write(contenido)  # Escribe el contenido en el archivo
        f.close()  # Cierra el archivo
        print('Archivo Graphviz generado: ' + nombre_completo + '\n')  # Imprime un mensaje de confirmación
