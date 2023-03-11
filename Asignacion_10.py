
#Asignacion.py
#Asignación_#10. Implementar el algortitmo de BFS parte2
#Implementar por completo el algoritmo de BFS
#Es necesario que una ves que se construye en árbol, se busquen todas las rutas de los n-1 nodos hacia la raíz (ó de la raiz hacia los n-1 nodos).
import Asignacion_9 as init
from Asignacion_8_1 import leer_grafo as lg

def BFS(G,s):
    colors,d,pi,q=init.init_BFS(G,s)
    while(q):
        u = q.pop(0)
        #print(G)
        for v in range(0,len(G[u]),2):
            #print(G[u][v])
            if colors[G[u][v]]=='white':
                colors[G[u][v]] = 'gray'
                d[G[u][v]] = d[u]+1
                pi[G[u][v]]= u
                q.append(G[u][v])
                #print(q)
        colors[u]='black'
    return colors,d,pi,q

def rutas(pi, i, l):
    l.append(i)
    if pi[i]!= None:
        rutas(pi,pi[i],l)
        
    return l
    
if __name__=='__main__':
    g =lg('ejemplo1.txt')
    print(BFS(g,2))

                    