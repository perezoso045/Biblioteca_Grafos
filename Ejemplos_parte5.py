from Metodos import *
from Ejemplos_parte1 import n1,n2,n3,p,r,d
nodo_raiz_1=20
nodo_raiz_2=5
nodo_raiz_3=29

# Grafo en forma de malla - 100 nodos
malla=Grafo('Malla de 25 por 4')  # Inicializa un grafo con el nombre correspondiente
malla.cargar_grafo('Archivos_GV/Malla de 25 por 4.gv') #Carga el grafo desde un archivo .gv
spring=malla.Calcular_fuerzas(0.05,0.05,1500,1,0.5,30)

#Grafo en forma de malla - 500 nodos
malla=Grafo('Malla de 50 por 10')  # Inicializa un grafo con el nombre correspondiente
malla.cargar_grafo('Archivos_GV/Malla de 50 por 10.gv') #Carga el grafo desde un archivo .gv
spring=malla.Calcular_fuerzas(1,1.2,500,0.55,15,13)

# Grafo de Erdos-Renyi - 100 nodos
erdosReny=Grafo('Erdos-Renyi de ' + str(n2) + ' nodos y ' + str(int(n2+(n2*1/3))) + ' aristas')  # Inicializa un grafo con el nombre correspondiente
erdosReny.cargar_grafo('Archivos_GV/Erdos-Renyi de '+ str(n2)+ ' nodos y ' + str(int(n2+(n2*2))) + ' aristas.gv') #Carga el grafo desde un archivo .gv
spring=erdosReny.Calcular_fuerzas(40,1.5,2000,0.5,1,1)

# Grafo de Erdos-Renyi - 500 nodos
erdosReny=Grafo('Erdos-Renyi de ' + str(n3) + ' nodos y ' + str(int(n3+(n3*1/3))) + ' aristas')  # Inicializa un grafo con el nombre correspondiente
erdosReny.cargar_grafo('Archivos_GV/Erdos-Renyi de '+ str(n3)+ ' nodos y ' + str(int(n3+(n3*1/3))) + ' aristas .gv') #Carga el grafo desde un archivo .gv
spring=erdosReny.Calcular_fuerzas(30,18,2000,10,6,10)


# Grafo de Gilbert - 100 nodos
gilbert=Grafo('Gilbert de ' + str(n2) + ' nodos y probabilidad de conexion de ' + str(p))  # Inicializa un grafo con el nombre correspondiente
gilbert.cargar_grafo('Archivos_GV/Gilbert de '+str(n2)+' nodos y probabilidad de conexion de '+str(p)+'.gv') #Carga el grafo desde un archivo .gv
spring=gilbert.Calcular_fuerzas(1000,1,2000,10,3,30)

# Grafo de Gilbert - 500 nodos
gilbert=Grafo('Gilbert de ' + str(n3) + ' nodos y probabilidad de conexion de ' + str(p))  # Inicializa un grafo con el nombre correspondiente
gilbert.cargar_grafo('Archivos_GV/Gilbert de '+str(n3)+' nodos y probabilidad de conexion de '+str(p)+'.gv') #Carga el grafo desde un archivo .gv
spring=gilbert.Calcular_fuerzas(1000,1,2000,10,10,1)

# Grafo geográfico - 100 nodos
geografico=Grafo('Geografico de ' + str(n2) + ' nodos y distancia ' + str(r))  # Inicializa un grafo con el nombre correspondiente
geografico.cargar_grafo('Archivos_GV/Geografico de '+str(n2)+' nodos y distancia '+str(r)+'.gv') #Carga el grafo desde un archivo .gv
spring=geografico.Calcular_fuerzas(450,1,1000,1,1,10)

# Grafo geográfico - 500 nodos
geografico=Grafo('Geografico de ' + str(n3) + ' nodos y distancia ' + str(r))  # Inicializa un grafo con el nombre correspondiente
geografico.cargar_grafo('Archivos_GV/Geografico de '+str(n3)+' nodos y distancia '+str(r)+'.gv') #Carga el grafo desde un archivo .gv
spring=geografico.Calcular_fuerzas(450,1,2000,1,50,1)


# Grafo Barabasi-Albert - 100 nodos
barabasiAlbert=Grafo('BarabasiAlbert de ' + str(n2) + ' nodos de grado ' + str(d))  # Inicializa un grafo con el nombre correspondiente
barabasiAlbert.cargar_grafo('Archivos_GV/BarabasiAlbert de '+str(n2)+' nodos de grado '+str(d)+'.gv') #Carga el grafo desde un archivo .gv
spring=barabasiAlbert.Calcular_fuerzas(1,1,1000,1,1,30)

# Grafo Barabasi-Albert - 500 nodos
barabasiAlbert=Grafo('BarabasiAlbert de ' + str(n3) + ' nodos de grado ' + str(d))  # Inicializa un grafo con el nombre correspondiente
barabasiAlbert.cargar_grafo('Archivos_GV/BarabasiAlbert de '+str(n3)+' nodos de grado '+str(d)+'.gv') #Carga el grafo desde un archivo .gv
spring=barabasiAlbert.Calcular_fuerzas(20,15,1000,10,10,5)

# Grafo Dorogovtsev-Mendes - 100 nodos
dorogovtsevMendes=Grafo('DorogovtsevMendes de ' + str(n2) + ' nodos')  # Inicializa un grafo con el nombre correspondiente
dorogovtsevMendes.cargar_grafo('Archivos_GV/DorogovtsevMendes de '+str(n2)+' nodos.gv') #Carga el grafo desde un archivo .gv
spring=dorogovtsevMendes.Calcular_fuerzas(5,1,1500,1,1,50)

# Grafo Dorogovtsev-Mendes - 500 nodos
orogovtsevMendes=Grafo('DorogovtsevMendes de ' + str(n3) + ' nodos')  # Inicializa un grafo con el nombre correspondiente
orogovtsevMendes.cargar_grafo('Archivos_GV/DorogovtsevMendes de '+str(n3)+' nodos.gv') #Carga el grafo desde un archivo .gv
pring=dorogovtsevMendes.Calcular_fuerzas(25,15,1500,10,10,1)
#