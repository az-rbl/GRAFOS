# Asignacion_12.py
# Asignación_#12. Implementar el algoritmo de Dijkstra

from Asignacion_8_1 import leer_grafo
from Asignacion_9 import init_BFS

def extract_min(q,g,s):
    for i in q:
        

if __name__ =='__main__':
    g =leer_grafo('ejemplo1.txt')
    colors,d,pi,q=init_BFS(g,0)
    q = [x for x in range(len(g))]
    s = []
    while q!= 0:
        



    print(colors,d,pi,q)
    