from Grafo import Grafo  # Importa la clase Grafo para crear y manipular grafos
import random, math  # Importa módulos para generar números aleatorios y realizar cálculos matemáticos

def Malla(m, n):
    # Crea un grafo en forma de malla de tamaño m x n.
    obj = Grafo('Malla de ' + str(m) + ' por ' + str(n))  # Inicializa un grafo con el nombre correspondiente
    for i in range(1, (m * n) + 1):
        obj.agregar_nodo(i)  # Agrega nodos al grafo numerados del 1 al m*n
    matriz = [[(i * m + j + 1) for j in range(m)] for i in range(n)]  # Crea una matriz para representar la malla
    for i in range(n):
        for j in range(m):
            num = matriz[i][j]  # Obtiene el número del nodo actual
            movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Posibles movimientos (arriba, abajo, izquierda, derecha)
            for di, dj in movimientos:
                ni, nj = i + di, j + dj  # Calcula la posición del nodo vecino
                if (0 <= ni < n) and (0 <= nj < m):  # Verifica si el vecino está dentro de los límites
                    obj.agregar_arista(num, matriz[ni][nj])  # Agrega una arista entre el nodo actual y el vecino
    return obj  # Retorna el grafo creado

def ErdosRenyi(n, a):
    # Crea un grafo aleatorio de Erdos-Renyi con n nodos y a aristas.
    obj = Grafo('Erdos-Renyi de ' + str(n) + ' nodos y ' + str(a) + ' aristas ')  # Inicializa el grafo
    for i in range(n):
        obj.agregar_nodo(i)  # Agrega nodos al grafo
    cont = 0  # Contador de aristas
    while(cont < a):  # Continúa hasta que se agreguen 'a' aristas
        n1 = random.randint(0, n - 1)  # Selecciona un nodo aleatorio
        n2 = random.randint(0, n - 1)  # Selecciona otro nodo aleatorio
        if n1 == n2:
            continue  # Evita conexiones entre el mismo nodo
        if not obj.repetida(n1, n2):  # Verifica que la arista no sea repetida
            obj.agregar_arista(n1, n2)  # Agrega la arista
            cont += 1  # Incrementa el contador
    return obj  # Retorna el grafo creado

def Gilbert(n, p):
    # Crea un grafo aleatorio de Gilbert con n nodos y probabilidad p de conexión.
    obj = Grafo('Gilbert de ' + str(n) + ' nodos y probabilidad de conexion de ' + str(p))  # Inicializa el grafo
    for i in range(n):
        obj.agregar_nodo(i)  # Agrega nodos al grafo
    for n1 in obj.nodos:
        for n2 in obj.nodos:
            if n1 != n2 and not obj.repetida(n1, n2):  # Asegura que no se conecte al mismo nodo
                if random.random() < p:  # Verifica si se debe conectar según la probabilidad p
                    obj.agregar_arista(n1, n2)  # Agrega la arista
    return obj  # Retorna el grafo creado

def Geografico(n, r):
    # Crea un grafo aleatorio basado en la distancia con n nodos y distancia r.
    obj = Grafo('Geografico de ' + str(n) + ' nodos y distancia ' + str(r))  # Inicializa el grafo
    corde = {}  # Diccionario para almacenar las coordenadas de los nodos
    for i in range(n):
        obj.agregar_nodo(i)  # Agrega nodos al grafo
        corde[i] = {random.random(), random.random()}  # Asigna coordenadas aleatorias (x, y) a cada nodo
    for n1 in corde:
        for n2 in corde:
            if n1 != n2 and not obj.repetida(n1, n2):  # Asegura que no se conecte al mismo nodo
                x1, y1 = corde[n1]  # Coordenadas del nodo n1
                x2, y2 = corde[n2]  # Coordenadas del nodo n2
                if math.sqrt((x2 - x1)**2 + (y2 - y1)**2) <= r:  # Verifica si la distancia entre n1 y n2 es <= r
                    obj.agregar_arista(n1, n2)  # Agrega la arista
    return obj  # Retorna el grafo creado

def BarabasiAlbert(n, d):
    # Crea un grafo de Barabasi-Albert con n nodos y grado d.
    obj = Grafo('BarabasiAlbert de ' + str(n) + ' nodos de grado ' + str(d))  # Inicializa el grafo
    for i in range(n):
        obj.agregar_nodo(i)  # Agrega nodos al grafo
    for i in range(d):
        for j in range(d):
            if i != j and not obj.repetida(i, j):  # Evita conectar el mismo nodo
                obj.agregar_arista(i, j)  # Conecta nodos iniciales
    for n1 in obj.nodos:
        for n2 in obj.nodos:
            if n1 != n2 and obj.grado(n1) < d and obj.grado(n2) < d and not obj.repetida(n1, n2):
                # Verifica que los nodos no excedan el grado d
                if random.random() < 1 - (obj.grado(n2) / d):  # Proporción de conectividad
                    obj.agregar_arista(n1, n2)  # Agrega la arista
    return obj  # Retorna el grafo creado

def DorogovtsevMendes(n):
    # Crea un grafo de Dorogovtsev-Mendes con n nodos.
    obj = Grafo('DorogovtsevMendes de ' + str(n) + ' nodos ')  # Inicializa el grafo
    for i in range(n):
        obj.agregar_nodo(i)  # Agrega nodos al grafo
    obj.agregar_arista(0, 1)  # Conecta los primeros nodos
    obj.agregar_arista(1, 2)
    obj.agregar_arista(2, 0)
    aux = 3  # Comienza a agregar más nodos
    while aux < n:
        aristasDisponibles = list(obj.aristas.keys())  # Obtiene una lista de aristas disponibles
        aleatorio = random.randint(0, obj.total_aristas() - 1)  # Selecciona una arista aleatoria
        extremo1 = obj.aristas[aristasDisponibles[aleatorio]].n1.id  # Obtiene un extremo de la arista
        extremo2 = obj.aristas[aristasDisponibles[aleatorio]].n2.id  # Obtiene el otro extremo
        obj.agregar_arista(aux, extremo1)  # Conecta el nuevo nodo a uno de los extremos
        obj.agregar_arista(aux, extremo2)  # Conecta el nuevo nodo al otro extremo
        aux += 1  # Avanza al siguiente nodo
    return obj  # Retorna el grafo creado

    



    
    
  
