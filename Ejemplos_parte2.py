from Metodos import *
from Ejemplos_parte1 import n1,n2,n3,p,r,d
nodo_raiz_1=20
nodo_raiz_2=5
nodo_raiz_3=29
# Grafo en forma de malla - 30 nodos
malla=Grafo('Malla de 6 por 5')  # Inicializa un grafo con el nombre correspondiente
malla.cargar_grafo('Archivos_GV/Malla de 6 por 5.gv') #Carga el grafo desde un archivo .gv
dfs_i=malla.DFS_iterativo(nodo_raiz_2) #Nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=malla.DFS_recursivo(nodo_raiz_2) #Nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=malla.BFS(nodo_raiz_2) #Nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo en forma de malla - 100 nodos
malla=Grafo('Malla de 25 por 4')  # Inicializa un grafo con el nombre correspondiente
malla.cargar_grafo('Archivos_GV/Malla de 25 por 4.gv') #Carga el grafo desde un archivo .gv
dfs_i=malla.DFS_iterativo(nodo_raiz_1) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=malla.DFS_recursivo(nodo_raiz_1) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=malla.BFS(nodo_raiz_1) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo en forma de malla - 500 nodos
malla=Grafo('Malla de 50 por 10')  # Inicializa un grafo con el nombre correspondiente
malla.cargar_grafo('Archivos_GV/Malla de 50 por 10.gv') #Carga el grafo desde un archivo .gv
dfs_i=malla.DFS_iterativo(nodo_raiz_1) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=malla.DFS_recursivo(nodo_raiz_1) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=malla.BFS(nodo_raiz_1) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo de Erdos-Renyi - 30 nodos
erdosReny=Grafo('Erdos-Renyi de ' + str(n1) + ' nodos y ' + str(int(n1+(n1*1/3))) + ' aristas ')  # Inicializa un grafo con el nombre correspondiente
erdosReny.cargar_grafo('Archivos_GV/Erdos-Renyi de '+ str(n1)+ ' nodos y ' + str(int(n1+(n1*1/3))) + ' aristas .gv') #Carga el grafo desde un archivo .gv
dfs_i=erdosReny.DFS_iterativo(nodo_raiz_2) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=erdosReny.DFS_recursivo(nodo_raiz_2) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=erdosReny.BFS(nodo_raiz_2) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo de Erdos-Renyi - 100 nodos
erdosReny=Grafo('Erdos-Renyi de ' + str(n2) + ' nodos y ' + str(int(n2+(n2*1/3))) + ' aristas ')  # Inicializa un grafo con el nombre correspondiente
erdosReny.cargar_grafo('Archivos_GV/Erdos-Renyi de '+ str(n2)+ ' nodos y ' + str(int(n2+(n2*1/3))) + ' aristas .gv') #Carga el grafo desde un archivo .gv
dfs_i=erdosReny.DFS_iterativo(nodo_raiz_1) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=erdosReny.DFS_recursivo(nodo_raiz_1) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=erdosReny.BFS(nodo_raiz_1) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo de Erdos-Renyi - 500 nodos
erdosReny=Grafo('Erdos-Renyi de ' + str(n3) + ' nodos y ' + str(int(n3+(n3*1/3))) + ' aristas ')  # Inicializa un grafo con el nombre correspondiente
erdosReny.cargar_grafo('Archivos_GV/Erdos-Renyi de '+ str(n3)+ ' nodos y ' + str(int(n3+(n3*1/3))) + ' aristas .gv') #Carga el grafo desde un archivo .gv
dfs_i=erdosReny.DFS_iterativo(nodo_raiz_1) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=erdosReny.DFS_recursivo(nodo_raiz_1) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=erdosReny.BFS(nodo_raiz_1) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo de Gilbert - 30 nodos
gilbert=Grafo('Gilbert de ' + str(n1) + ' nodos y probabilidad de conexion de ' + str(p))  # Inicializa un grafo con el nombre correspondiente
gilbert.cargar_grafo('Archivos_GV/Gilbert de '+str(n1)+' nodos y probabilidad de conexion de '+str(p)+'.gv') #Carga el grafo desde un archivo .gv
dfs_i=gilbert.DFS_iterativo(nodo_raiz_2) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=gilbert.DFS_recursivo(nodo_raiz_2) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=gilbert.BFS(nodo_raiz_2) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo de Gilbert - 100 nodos
gilbert=Grafo('Gilbert de ' + str(n2) + ' nodos y probabilidad de conexion de ' + str(p))  # Inicializa un grafo con el nombre correspondiente
gilbert.cargar_grafo('Archivos_GV/Gilbert de '+str(n2)+' nodos y probabilidad de conexion de '+str(p)+'.gv') #Carga el grafo desde un archivo .gv
dfs_i=gilbert.DFS_iterativo(nodo_raiz_1) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=gilbert.DFS_recursivo(nodo_raiz_1) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=gilbert.BFS(nodo_raiz_1) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo de Gilbert - 500 nodos
gilbert=Grafo('Gilbert de ' + str(n3) + ' nodos y probabilidad de conexion de ' + str(p))  # Inicializa un grafo con el nombre correspondiente
gilbert.cargar_grafo('Archivos_GV/Gilbert de '+str(n3)+' nodos y probabilidad de conexion de '+str(p)+'.gv') #Carga el grafo desde un archivo .gv
dfs_i=gilbert.DFS_iterativo(nodo_raiz_1) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=gilbert.DFS_recursivo(nodo_raiz_1) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=gilbert.BFS(nodo_raiz_1) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo geográfico - 30 nodos
geografico=Grafo('Geografico de ' + str(n1) + ' nodos y distancia ' + str(r))  # Inicializa un grafo con el nombre correspondiente
geografico.cargar_grafo('Archivos_GV/Geografico de '+str(n1)+' nodos y distancia '+str(r)+'.gv') #Carga el grafo desde un archivo .gv
dfs_i=geografico.DFS_iterativo(nodo_raiz_3) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=geografico.DFS_recursivo(nodo_raiz_3) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=geografico.BFS(nodo_raiz_3) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo geográfico - 100 nodos
geografico=Grafo('Geografico de ' + str(n2) + ' nodos y distancia ' + str(r))  # Inicializa un grafo con el nombre correspondiente
geografico.cargar_grafo('Archivos_GV/Geografico de '+str(n2)+' nodos y distancia '+str(r)+'.gv') #Carga el grafo desde un archivo .gv
dfs_i=geografico.DFS_iterativo(nodo_raiz_3) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=geografico.DFS_recursivo(nodo_raiz_3) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=geografico.BFS(nodo_raiz_3) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo geográfico - 500 nodos
geografico=Grafo('Geografico de ' + str(n3) + ' nodos y distancia ' + str(r))  # Inicializa un grafo con el nombre correspondiente
geografico.cargar_grafo('Archivos_GV/Geografico de '+str(n3)+' nodos y distancia '+str(r)+'.gv') #Carga el grafo desde un archivo .gv
dfs_i=geografico.DFS_iterativo(nodo_raiz_3) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=geografico.DFS_recursivo(nodo_raiz_3) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=geografico.BFS(nodo_raiz_3) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo Barabasi-Albert - 30 nodos
barabasiAlbert=Grafo('BarabasiAlbert de ' + str(n1) + ' nodos de grado ' + str(d))  # Inicializa un grafo con el nombre correspondiente
barabasiAlbert.cargar_grafo('Archivos_GV/BarabasiAlbert de '+str(n1)+' nodos de grado '+str(d)+'.gv') #Carga el grafo desde un archivo .gv
dfs_i=barabasiAlbert.DFS_iterativo(nodo_raiz_2) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=barabasiAlbert.DFS_recursivo(nodo_raiz_2) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=barabasiAlbert.BFS(nodo_raiz_2) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo Barabasi-Albert - 100 nodos
barabasiAlbert=Grafo('BarabasiAlbert de ' + str(n2) + ' nodos de grado ' + str(d))  # Inicializa un grafo con el nombre correspondiente
barabasiAlbert.cargar_grafo('Archivos_GV/BarabasiAlbert de '+str(n2)+' nodos de grado '+str(d)+'.gv') #Carga el grafo desde un archivo .gv
dfs_i=barabasiAlbert.DFS_iterativo(nodo_raiz_1) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=barabasiAlbert.DFS_recursivo(nodo_raiz_1) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=barabasiAlbert.BFS(nodo_raiz_1) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo Barabasi-Albert - 500 nodos
barabasiAlbert=Grafo('BarabasiAlbert de ' + str(n3) + ' nodos de grado ' + str(d))  # Inicializa un grafo con el nombre correspondiente
barabasiAlbert.cargar_grafo('Archivos_GV/BarabasiAlbert de '+str(n3)+' nodos de grado '+str(d)+'.gv') #Carga el grafo desde un archivo .gv
dfs_i=barabasiAlbert.DFS_iterativo(nodo_raiz_1) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=barabasiAlbert.DFS_recursivo(nodo_raiz_1) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=barabasiAlbert.BFS(nodo_raiz_1) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo Dorogovtsev-Mendes - 30 nodos
dorogovtsevMendes=Grafo('DorogovtsevMendes de ' + str(n1) + ' nodos ')  # Inicializa un grafo con el nombre correspondiente
dorogovtsevMendes.cargar_grafo('Archivos_GV/DorogovtsevMendes de '+str(n1)+' nodos.gv') #Carga el grafo desde un archivo .gv
dfs_i=dorogovtsevMendes.DFS_iterativo(nodo_raiz_2) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=dorogovtsevMendes.DFS_recursivo(nodo_raiz_2) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=dorogovtsevMendes.BFS(nodo_raiz_2) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo Dorogovtsev-Mendes - 100 nodos
dorogovtsevMendes=Grafo('DorogovtsevMendes de ' + str(n2) + ' nodos ')  # Inicializa un grafo con el nombre correspondiente
dorogovtsevMendes.cargar_grafo('Archivos_GV/DorogovtsevMendes de '+str(n2)+' nodos.gv') #Carga el grafo desde un archivo .gv
dfs_i=dorogovtsevMendes.DFS_iterativo(nodo_raiz_1) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=dorogovtsevMendes.DFS_recursivo(nodo_raiz_1) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=dorogovtsevMendes.BFS(nodo_raiz_1) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo

# Grafo Dorogovtsev-Mendes - 500 nodos
dorogovtsevMendes=Grafo('DorogovtsevMendes de ' + str(n3) + ' nodos ')  # Inicializa un grafo con el nombre correspondiente
dorogovtsevMendes.cargar_grafo('Archivos_GV/DorogovtsevMendes de '+str(n3)+' nodos.gv') #Carga el grafo desde un archivo .gv
dfs_i=dorogovtsevMendes.DFS_iterativo(nodo_raiz_1) #nodo raiz 
dfs_i.graficar()  # Genera un archivo para graficar el grafo
dfs_r=dorogovtsevMendes.DFS_recursivo(nodo_raiz_1) #nodo raiz 
dfs_r.graficar()  # Genera un archivo para graficar el grafo
bfs=dorogovtsevMendes.BFS(nodo_raiz_1) #nodo raiz 
bfs.graficar()  # Genera un archivo para graficar el grafo