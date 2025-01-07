import pygame
class Quadtree:
    # Inicializa la estructura del quadtree con el límite (boundary) y la capacidad máxima de puntos
    def __init__(self, boundary, capacity):
        self.boundary = boundary  # Limites del área que abarca este nodo (como un rectángulo)
        self.capacity = capacity  # Capacidad máxima de puntos antes de subdividirse
        self.points = []  # Lista de puntos que están dentro de este nodo
        self.divided = False  # Indicador de si el nodo ha sido subdividido
        self.nw = self.ne = self.sw = self.se = None  # Los 4 sub-nodos, inicialmente None

    # Método para insertar un punto en el quadtree
    def insert(self, point):
        x, y = point  # Coordenadas del punto a insertar
        x_min, y_min, x_max, y_max = self.boundary  # Limites del área actual

        # Verifica si el punto está dentro del límite del nodo
        if x < x_min or x > x_max or y < y_min or y > y_max:
            return False  # El punto no está dentro del límite

        # Si la capacidad no ha sido alcanzada, se agrega el punto
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True  # Punto insertado correctamente

        # Si ya se ha alcanzado la capacidad máxima y el nodo no ha sido subdividido, se subdivide
        if not self.divided:
            self.subdivide()

        # Intentar insertar el punto en cada uno de los sub-nodos
        if self.nw.insert(point): return True
        if self.ne.insert(point): return True
        if self.sw.insert(point): return True
        if self.se.insert(point): return True

        return False  # El punto no pudo ser insertado (aunque no debería ocurrir en este contexto)

    # Método para subdividir el nodo en 4 sub-nodos
    def subdivide(self):
        x_min, y_min, x_max, y_max = self.boundary  # Limites del nodo actual
        mid_x = (x_min + x_max) / 2  # Coordenada media en X
        mid_y = (y_min + y_max) / 2  # Coordenada media en Y

        # Crear los límites para los 4 sub-nodos
        nw_boundary = (x_min, y_min, mid_x, mid_y)
        ne_boundary = (mid_x, y_min, x_max, mid_y)
        sw_boundary = (x_min, mid_y, mid_x, y_max)
        se_boundary = (mid_x, mid_y, x_max, y_max)

        # Crear los sub-nodos (4 cuadrantes)
        self.nw = Quadtree(nw_boundary, self.capacity)
        self.ne = Quadtree(ne_boundary, self.capacity)
        self.sw = Quadtree(sw_boundary, self.capacity)
        self.se = Quadtree(se_boundary, self.capacity)

        # Reinsertar los puntos actuales en los sub-nodos
        for point in self.points:
            self.nw.insert(point)
            self.ne.insert(point)
            self.sw.insert(point)
            self.se.insert(point)

        self.points = []  # Limpiar la lista de puntos del nodo actual, ya que han sido reasignados
        self.divided = True  # Marcar que el nodo se ha subdividido

    # Método para realizar una consulta y obtener los puntos dentro de una región dada
    def query(self, region):
        x_min, y_min, x_max, y_max = region  # Limites de la región de consulta
        result = []  # Lista para almacenar los puntos que coinciden con la región de consulta

        # Limites del área actual
        q_x_min, q_y_min, q_x_max, q_y_max = self.boundary

        # Si la región no se solapa con el área actual, no hay nada que consultar
        if x_max < q_x_min or x_min > q_x_max or y_max < q_y_min or y_min > q_y_max:
            return result

        # Verificar si los puntos en el nodo actual están dentro de la región de consulta
        for point in self.points:
            if x_min <= point[0] <= x_max and y_min <= point[1] <= y_max:
                result.append(point)  # Agregar punto que cae dentro de la región

        # Si el nodo ha sido subdividido, consultar en los sub-nodos
        if self.divided:
            result.extend(self.nw.query(region))  # Consultar en el sub-nodo noroeste
            result.extend(self.ne.query(region))  # Consultar en el sub-nodo noreste
            result.extend(self.sw.query(region))  # Consultar en el sub-nodo suroeste
            result.extend(self.se.query(region))  # Consultar en el sub-nodo sureste

        return result  # Devolver los puntos que se encuentran dentro de la región solicitada

   # Método para dibujar los límites del Quadtree (cuadrantes)
    def dibujar(self, screen, color):
        # Dibujar el rectángulo que representa el límite del nodo actual
        x_min, y_min, x_max, y_max = self.boundary
        pygame.draw.rect(screen, color, pygame.Rect(x_min, y_min, x_max - x_min, y_max - y_min), 1)

        # Dibujar las divisiones si el Quadtree ha sido subdividido
        if self.divided:
            self.nw.dibujar(screen, color)  # Dibujar sub-nodo noroeste
            self.ne.dibujar(screen, color)  # Dibujar sub-nodo noreste
            self.sw.dibujar(screen, color)  # Dibujar sub-nodo suroeste
            self.se.dibujar(screen, color)  # Dibujar sub-nodo sureste