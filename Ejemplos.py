from metodos import *  # Importa todas las funciones del módulo 'metodos'

# Grafo en forma de malla - 30 nodos
malla = Malla(6, 5)  # Crea un grafo de malla de 6 filas y 5 columnas
malla.graficar()  # Genera un archivo para graficar el grafo

# Grafo en forma de malla - 100 nodos
malla = Malla(25, 4)  # Crea un grafo de malla de 25 filas y 4 columnas
malla.graficar()  # Genera el gráfico

# Grafo en forma de malla - 500 nodos
malla = Malla(50, 10)  # Crea un grafo de malla de 50 filas y 10 columnas
malla.graficar()  # Genera el gráfico

# Grafo de Erdos-Renyi - 30 nodos
erdosReny = ErdosRenyi(n=30, a=30)  # Crea un grafo Erdos-Renyi con 30 nodos y 30 aristas
erdosReny.graficar()  # Genera el gráfico

# Grafo de Erdos-Renyi - 100 nodos
erdosReny = ErdosRenyi(n=100, a=100)  # Crea un grafo Erdos-Renyi con 100 nodos y 100 aristas
erdosReny.graficar()  # Genera el gráfico

# Grafo de Erdos-Renyi - 500 nodos
erdosReny = ErdosRenyi(n=500, a=500)  # Crea un grafo Erdos-Renyi con 500 nodos y 500 aristas
erdosReny.graficar()  # Genera el gráfico

# Grafo de Gilbert - 30 nodos
gilbert = Gilbert(n=30, p=0.1)  # Crea un grafo de Gilbert con 30 nodos y probabilidad de conexión 0.1
gilbert.graficar()  # Genera el gráfico

# Grafo de Gilbert - 100 nodos
gilbert = Gilbert(n=100, p=0.1)  # Crea un grafo de Gilbert con 100 nodos y probabilidad de conexión 0.1
gilbert.graficar()  # Genera el gráfico

# Grafo de Gilbert - 500 nodos
gilbert = Gilbert(n=500, p=0.1)  # Crea un grafo de Gilbert con 500 nodos y probabilidad de conexión 0.1
gilbert.graficar()  # Genera el gráfico

# Grafo geográfico - 30 nodos
geografico = Geografico(n=30, r=0.1)  # Crea un grafo geográfico con 30 nodos y distancia 0.1
geografico.graficar()  # Genera el gráfico

# Grafo geográfico - 100 nodos
geografico = Geografico(n=100, r=0.1)  # Crea un grafo geográfico con 100 nodos y distancia 0.1
geografico.graficar()  # Genera el gráfico

# Grafo geográfico - 500 nodos
geografico = Geografico(n=500, r=0.1)  # Crea un grafo geográfico con 500 nodos y distancia 0.1
geografico.graficar()  # Genera el gráfico

# Grafo Barabasi-Albert - 30 nodos
barabasiAlbert = BarabasiAlbert(n=30, d=4)  # Crea un grafo de Barabasi-Albert con 30 nodos y grado 4
barabasiAlbert.graficar()  # Genera el gráfico

# Grafo Barabasi-Albert - 100 nodos
barabasiAlbert = BarabasiAlbert(n=100, d=4)  # Crea un grafo de Barabasi-Albert con 100 nodos y grado 4
barabasiAlbert.graficar()  # Genera el gráfico

# Grafo Barabasi-Albert - 500 nodos
barabasiAlbert = BarabasiAlbert(n=500, d=5)  # Crea un grafo de Barabasi-Albert con 500 nodos y grado 5
barabasiAlbert.graficar()  # Genera el gráfico

# Grafo Dorogovtsev-Mendes - 30 nodos
dorogovtsevMendes = DorogovtsevMendes(30)  # Crea un grafo de Dorogovtsev-Mendes con 30 nodos
dorogovtsevMendes.graficar()  # Genera el gráfico

# Grafo Dorogovtsev-Mendes - 100 nodos
dorogovtsevMendes = DorogovtsevMendes(100)  # Crea un grafo de Dorogovtsev-Mendes con 100 nodos
dorogovtsevMendes.graficar()  # Genera el gráfico

# Grafo Dorogovtsev-Mendes - 500 nodos
dorogovtsevMendes = DorogovtsevMendes(500)  # Crea un grafo de Dorogovtsev-Mendes con 500 nodos
dorogovtsevMendes.graficar()  # Genera el gráfico
