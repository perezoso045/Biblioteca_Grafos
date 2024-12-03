from Metodos import *
from Ejemplos_parte1 import n1,n2,n3,p,r,d
nodo_raiz_1=20
nodo_raiz_2=5
nodo_raiz_3=29

# Grafo en forma de malla - 30 nodos
malla=Grafo('Malla de 6 por 5 con pesos') 
malla.cargar_grafo('Archivos_GV/Malla de 6 por 5.gv') 
malla.graficar(True)  
kruskal=malla.Kruskal() 
kruskal.graficar(True)
kruskal_inverso=malla.Kruskal_inverso()
kruskal_inverso.graficar(True)
prim=malla.Prim(nodo_raiz_2)
prim.graficar(True)

# Grafo en forma de malla - 100 nodos
malla=Grafo('Malla de 25 por 4 con pesos')  # Inicializa un grafo con el nombre correspondiente
malla.cargar_grafo('Archivos_GV/Malla de 25 por 4.gv') #Carga el grafo desde un archivo .gv
malla.graficar(True)  
kruskal=malla.Kruskal() 
kruskal.graficar(True)
kruskal_inverso=malla.Kruskal_inverso()
kruskal_inverso.graficar(True)
prim=malla.Prim(nodo_raiz_1)
prim.graficar(True)

# Grafo de Erdos-Renyi - 30 nodos
erdosReny=Grafo('Erdos-Renyi de ' + str(n1) + ' nodos y ' + str(int(n1+(n1*0.7))) + ' aristas con pesos')  # Inicializa un grafo con el nombre correspondiente
erdosReny.cargar_grafo('Archivos_GV/Erdos-Renyi de '+ str(n1)+ ' nodos y ' + str(int(n1+(n1*0.7))) + ' aristas.gv') #Carga el grafo desde un archivo .gv
erdosReny.graficar(True)  # Genera un archivo para graficar el grafo
kruskal=erdosReny.Kruskal() 
kruskal.graficar(True)
kruskal_inverso=erdosReny.Kruskal_inverso()
kruskal_inverso.graficar(True)
prim=erdosReny.Prim(nodo_raiz_2)
prim.graficar(True)

# Grafo de Erdos-Renyi - 100 nodos
erdosReny=Grafo('Erdos-Renyi de ' + str(n2) + ' nodos y ' + str(int(n2+(n2*2))) + ' aristas con pesos')  # Inicializa un grafo con el nombre correspondiente
erdosReny.cargar_grafo('Archivos_GV/Erdos-Renyi de '+ str(n2)+ ' nodos y ' + str(int(n2+(n2*2))) + ' aristas.gv') #Carga el grafo desde un archivo .gv
erdosReny.graficar(True)  # Genera un archivo para graficar el grafo
kruskal=erdosReny.Kruskal() 
kruskal.graficar(True)
kruskal_inverso=erdosReny.Kruskal_inverso()
kruskal_inverso.graficar(True)
prim=erdosReny.Prim(nodo_raiz_1)
prim.graficar(True)

# Grafo de Gilbert - 30 nodos
gilbert=Grafo('Gilbert de ' + str(n1) + ' nodos y probabilidad de conexion de ' + str(p) +' con pesos')  # Inicializa un grafo con el nombre correspondiente
gilbert.cargar_grafo('Archivos_GV/Gilbert de '+str(n1)+' nodos y probabilidad de conexion de '+str(p)+'.gv') #Carga el grafo desde un archivo .gv
gilbert.graficar(True)  # Genera un archivo para graficar el grafo
kruskal=gilbert.Kruskal() 
kruskal.graficar(True)
kruskal_inverso=gilbert.Kruskal_inverso()
kruskal_inverso.graficar(True)
prim=gilbert.Prim(nodo_raiz_1)
prim.graficar(True)

# Grafo de Gilbert - 100 nodos
gilbert=Grafo('Gilbert de ' + str(n2) + ' nodos y probabilidad de conexion de ' + str(p)+' con pesos')  # Inicializa un grafo con el nombre correspondiente
gilbert.cargar_grafo('Archivos_GV/Gilbert de '+str(n2)+' nodos y probabilidad de conexion de '+str(p)+'.gv') #Carga el grafo desde un archivo .gv
gilbert.graficar(True)  # Genera un archivo para graficar el grafo
kruskal=gilbert.Kruskal() 
kruskal.graficar(True)
kruskal_inverso=gilbert.Kruskal_inverso()
kruskal_inverso.graficar(True)
prim=gilbert.Prim(nodo_raiz_1)
prim.graficar(True)

# Grafo geográfico - 30 nodos
geografico=Grafo('Geografico de ' + str(n1) + ' nodos y distancia ' + str(r)+' con pesos')  # Inicializa un grafo con el nombre correspondiente
geografico.cargar_grafo('Archivos_GV/Geografico de '+str(n1)+' nodos y distancia '+str(r)+'.gv') #Carga el grafo desde un archivo .gv
geografico.graficar(True)  # Genera un archivo para graficar el grafo
kruskal=geografico.Kruskal() 
kruskal.graficar(True)
kruskal_inverso=geografico.Kruskal_inverso()
kruskal_inverso.graficar(True)
prim=geografico.Prim(nodo_raiz_1)
prim.graficar(True)

# Grafo geográfico - 100 nodos
geografico=Grafo('Geografico de ' + str(n2) + ' nodos y distancia ' + str(r)+' con pesos')  # Inicializa un grafo con el nombre correspondiente
geografico.cargar_grafo('Archivos_GV/Geografico de '+str(n2)+' nodos y distancia '+str(r)+'.gv') #Carga el grafo desde un archivo .gv
geografico.graficar(True)  # Genera un archivo para graficar el grafo
kruskal=geografico.Kruskal() 
kruskal.graficar(True)
kruskal_inverso=geografico.Kruskal_inverso()
kruskal_inverso.graficar(True)
prim=geografico.Prim(nodo_raiz_1)
prim.graficar(True)

# Grafo Barabasi-Albert - 30 nodos
barabasiAlbert=Grafo('BarabasiAlbert de ' + str(n1) + ' nodos de grado ' + str(d)+' con pesos')  # Inicializa un grafo con el nombre correspondiente
barabasiAlbert.cargar_grafo('Archivos_GV/BarabasiAlbert de '+str(n1)+' nodos de grado '+str(d)+'.gv') #Carga el grafo desde un archivo .gv
barabasiAlbert.graficar(True)  # Genera un archivo para graficar el grafo
kruskal=barabasiAlbert.Kruskal() 
kruskal.graficar(True)
kruskal_inverso=barabasiAlbert.Kruskal_inverso()
kruskal_inverso.graficar(True)
prim=barabasiAlbert.Prim(nodo_raiz_1)
prim.graficar(True)

# Grafo Barabasi-Albert - 100 nodos
barabasiAlbert=Grafo('BarabasiAlbert de ' + str(n2) + ' nodos de grado ' + str(d)+' con pesos')  # Inicializa un grafo con el nombre correspondiente
barabasiAlbert.cargar_grafo('Archivos_GV/BarabasiAlbert de '+str(n2)+' nodos de grado '+str(d)+'.gv') #Carga el grafo desde un archivo .gv
barabasiAlbert.graficar(True)  # Genera un archivo para graficar el grafo
kruskal=barabasiAlbert.Kruskal() 
kruskal.graficar(True)
kruskal_inverso=barabasiAlbert.Kruskal_inverso()
kruskal_inverso.graficar(True)
prim=barabasiAlbert.Prim(nodo_raiz_1)
prim.graficar(True)

# Grafo Dorogovtsev-Mendes - 30 nodos
dorogovtsevMendes=Grafo('DorogovtsevMendes de ' + str(n1) + ' nodos con pesos')  # Inicializa un grafo con el nombre correspondiente
dorogovtsevMendes.cargar_grafo('Archivos_GV/DorogovtsevMendes de '+str(n1)+' nodos.gv') #Carga el grafo desde un archivo .gv
dorogovtsevMendes.graficar(True)  # Genera un archivo para graficar el grafo
kruskal=dorogovtsevMendes.Kruskal() 
kruskal.graficar(True)
kruskal_inverso=dorogovtsevMendes.Kruskal_inverso()
kruskal_inverso.graficar(True)
prim=dorogovtsevMendes.Prim(nodo_raiz_1)
prim.graficar(True)

# Grafo Dorogovtsev-Mendes - 100 nodos
dorogovtsevMendes=Grafo('DorogovtsevMendes de ' + str(n2) + ' nodos con pesos')  # Inicializa un grafo con el nombre correspondiente
dorogovtsevMendes.cargar_grafo('Archivos_GV/DorogovtsevMendes de '+str(n2)+' nodos.gv') #Carga el grafo desde un archivo .gv
dorogovtsevMendes.graficar(True)  # Genera un archivo para graficar el grafo
kruskal=dorogovtsevMendes.Kruskal() 
kruskal.graficar(True)
kruskal_inverso=dorogovtsevMendes.Kruskal_inverso()
kruskal_inverso.graficar(True)
prim=dorogovtsevMendes.Prim(nodo_raiz_1)
prim.graficar(True)