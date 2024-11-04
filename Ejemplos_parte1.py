from Metodos import *  # Importa todas las funciones del módulo 'metodos'
n1=30
n2=100
n3=500
p=0.5
r=0.5
d=5
if __name__ == "__main__":
    # Grafo en forma de malla - n1 nodos
    malla = Malla(6, 5)  # Crea un grafo de malla de 6 filas y 5 columnas
    malla.graficar()  # Genera un archivo para graficar el grafo
    
    # Grafo en forma de malla - n2 nodos
    malla = Malla(25, 4)  # Crea un grafo de malla de 25 filas y 4 columnas
    malla.graficar()  # Genera el gráfico
    
    # Grafo en forma de malla - n3 nodos
    malla = Malla(50, 10)  # Crea un grafo de malla de 50 filas y 10 columnas
    malla.graficar()  # Genera el gráfico
    
    # Grafo de Erdos-Renyi - n1 nodos
    erdosReny = ErdosRenyi(n=n1, a=int(n1+(n1*1/3))) # Crea un grafo Erdos-Renyi con n1 nodos y n1+1/3 aristas
    erdosReny.graficar()  # Genera el gráfico
    
    # Grafo de Erdos-Renyi - n2 nodos
    erdosReny = ErdosRenyi(n=n2, a=int(n2+(n2*1/3)))  # Crea un grafo Erdos-Renyi con n2 nodos y n2+1/3 aristas
    erdosReny.graficar()  # Genera el gráfico
    
    # Grafo de Erdos-Renyi - n3 nodos
    erdosReny = ErdosRenyi(n=n3, a=int(n3+(n3*1/3)))  # Crea un grafo Erdos-Renyi con n3 nodos y n3+1/3 aristas
    erdosReny.graficar()  # Genera el gráfico
    
    # Grafo de Gilbert - n1 nodos
    gilbert = Gilbert(n=n1, p=p)  # Crea un grafo de Gilbert con n1 nodos y probabilidad de conexión p
    gilbert.graficar()  # Genera el gráfico
    
    # Grafo de Gilbert - n2 nodos
    gilbert = Gilbert(n=n2, p=p)  # Crea un grafo de Gilbert con n2 nodos y probabilidad de conexión p
    gilbert.graficar()  # Genera el gráfico
    
    # Grafo de Gilbert - n3 nodos
    gilbert = Gilbert(n=n3, p=p)  # Crea un grafo de Gilbert con n3 nodos y probabilidad de conexión p
    gilbert.graficar()  # Genera el gráfico
    
    # Grafo geográfico - n1 nodos
    geografico = Geografico(n=n1, r=r)  # Crea un grafo geográfico con n1 nodos y distancia r
    geografico.graficar()  # Genera el gráfico
    
    # Grafo geográfico - n2 nodos
    geografico = Geografico(n=n2, r=r)  # Crea un grafo geográfico con n2 nodos y distancia r
    geografico.graficar()  # Genera el gráfico
    
    # Grafo geográfico - n3 nodos
    geografico = Geografico(n=n3, r=r)  # Crea un grafo geográfico con n3 nodos y distancia r
    geografico.graficar()  # Genera el gráfico
    
    # Grafo Barabasi-Albert - n1 nodos
    barabasiAlbert = BarabasiAlbert(n=n1, d=d)  # Crea un grafo de Barabasi-Albert con n1 nodos y grado d
    barabasiAlbert.graficar()  # Genera el gráfico
    
    # Grafo Barabasi-Albert - n2 nodos
    barabasiAlbert = BarabasiAlbert(n=n2, d=d)  # Crea un grafo de Barabasi-Albert con n2 nodos y grado d
    barabasiAlbert.graficar()  # Genera el gráfico
    
    # Grafo Barabasi-Albert - n3 nodos
    barabasiAlbert = BarabasiAlbert(n=n3, d=d)  # Crea un grafo de Barabasi-Albert con n3 nodos y grado d
    barabasiAlbert.graficar()  # Genera el gráfico
    
    # Grafo Dorogovtsev-Mendes - n1 nodos
    dorogovtsevMendes = DorogovtsevMendes(n1)  # Crea un grafo de Dorogovtsev-Mendes con n1 nodos
    dorogovtsevMendes.graficar()  # Genera el gráfico
    
    # Grafo Dorogovtsev-Mendes - n2 nodos
    dorogovtsevMendes = DorogovtsevMendes(n2)  # Crea un grafo de Dorogovtsev-Mendes con n2 nodos
    dorogovtsevMendes.graficar()  # Genera el gráfico
    
    # Grafo Dorogovtsev-Mendes - n3 nodos
    dorogovtsevMendes = DorogovtsevMendes(n3)  # Crea un grafo de Dorogovtsev-Mendes con n3 nodos
    dorogovtsevMendes.graficar()  # Genera el gráfico
    