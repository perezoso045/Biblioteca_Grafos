class Nodo:
    def __init__(self, id):
        # Inicializa un nodo con un identificador único (id).
        # El atributo 'grado' se establece en 0, indicando que el nodo no tiene conexiones al inicio.
        self.id = id
        self.grado = 0

        #Parametros algoritmo de dijkstra
        self.padre=None
        self.distancia=float('inf')

    def __str__(self):
        # Devuelve una representación en forma de cadena del nodo, que es su identificador (id).
        return str(self.id)
    def __eq__(self, otroNodo):
      return self.id == otroNodo.id
    def __lt__(self, otroNodo):
      return self.distancia < otroNodo.distancia

