
#Asignacion_11.py
#Asignación_11. Implementar el algortitmo de BFS parte2
#En esta asignación se deben construir todos los áboles BFS, uno para cada uno de los nodos del grado selecccionado.
#Es necesario almacenar todas las rutas en alguna estructura de datos que pueda ser mostrada al final.

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

def todos_nodos(g):
    r =[]
    for i in range(len(g)):
        nl=[]
        r.append(nl)
        #print(f"padre {i}")
        colors,d,pi,q=BFS(g,i)
        for j in range(len(pi)):
            l=[]
            rut =rutas(pi,j,l)
            r[i].append(rut)
    return r






if __name__=='__main__':
    g =lg('ejemplo1.txt')
    r =todos_nodos(g)
    colors,d,pi,q = BFS(g,4)
    print(r)
    
    
                    