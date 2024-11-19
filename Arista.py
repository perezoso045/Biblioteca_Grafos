import random
class Arista:
    def __init__(self, n1, n2):
        # Inicializa la clase Arista con dos nodos, n1 y n2.
        self.n1 = n1  # Primer nodo de la arista
        self.n2 = n2  # Segundo nodo de la arista
        self.id = str(n1) + ' - ' + str(n2)  # Crea una representación única para la arista
        self.peso = random.randint(1,50)

    def __str__(self):
        # Devuelve la representación en forma de cadena de la arista.
        return str(self.id)
