#Asignacion.py
#Asignación_#10. Implementar el algortitmo de BFS parte2
#Implementar por completo el algoritmo de BFS
#Es necesario que una ves que se construye en árbol, se busquen todas las rutas de los n-1 nodos hacia la raíz (ó de la raiz hacia los n-1 nodos).
import Asignacion_9 as init
from Asignacion_8_1 import leer_grafo as lg

def BFS(G,s):
    colors,d,pi,q=init.init_BFS(G,s)
    while(q):
        u = q.pop()
        for v in range(len(G[u])):
            if G[u][v] ==1:
                if colors[v]=='white':
                    colors[v] = 'gray'
                    d[v] = d[u]+1
                    pi[v]= u
                    q.append(v)
        colors[u]='black'
    return colors,d,pi,q
    
if __name__=='__main__':
    g =lg('ej_bfs.txt')
    print(BFS(g,2))
                    