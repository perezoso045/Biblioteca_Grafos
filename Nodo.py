class Nodo:
    def __init__(self, id):
        # Inicializa un nodo con un identificador único (id).
        # El atributo 'grado' se establece en 0, indicando que el nodo no tiene conexiones al inicio.
        self.id = id
        self.grado = 0

    def __str__(self):
        # Devuelve una representación en forma de cadena del nodo, que es su identificador (id).
        return str(self.id)
