
#Asignacion_13.py
#Asignación_13. Implementar el algortitmo de BFS parte2
#Esta asignación consiste en utlizar la librería de netwokx para pintar el grafo que se este utilizando y además pintar encima del grafo uno de los árboles construidos. 

import Asignacion_9 as init
import networkx as nx
import matplotlib.pyplot as plt
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

def dibujar(g, colors):
    
    G = nx.Graph()
    for j in range(len(colors)):
        G.add_node(j,node_color=colors[j])
    
    for i in range(len(g)):
        for j in range(0,len(g[i],),2):
            G.add_edge(g[i][j],i)
    #color_map =[color]
    #color_map =[node_color for node in G]
    #nx.draw(G, with_labels=True, node_color=colors, font_color= 'yellow')

    #plt.show()
    return G

def dibujar_arbol(r, d):
    G = nx.DiGraph()
    for j in range(len(d)):
        G.add_node(j,d=colors[j])
    for i in r:
        if len(i)>1:
            G.add_edge(i[1],i[0])
    # nx.draw(G, with_labels=True)
    # plt.show()
    return G





if __name__=='__main__':
    g =lg('ejemplo1.txt')
    r =todos_nodos(g)
    colors,d,pi,q = BFS(g,0)
    fig, all_axes = plt.subplots(1, 2)
    ax = all_axes.flat

    nx.draw(dibujar(g,colors), with_labels=True, node_color=colors, font_color= 'yellow',ax=ax[0])
    #Arbol con inicio en nodo 0
    G=dibujar_arbol(r[0], d)
    nx.draw(G, with_labels=True, ax=ax[1], node_color=d, arrows=True)
    plt.show()

    
   
                    