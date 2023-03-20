from Asignacion_8_1 import leer_grafo as lg
import networkx as nx
import matplotlib.pyplot as plt

def initialize_SS(G,s):
    d = [1000]*len(G)
    pi = [None]*len(G)
    d[s]=0
    return d,pi

#funcion que regresa el valor de peso mínimo de entre los nodos de la cola Q
def extract_min(Q,G,d):
    min_w = float('inf')
    for u in Q:
        if d[u] < min_w:
            min_w = d[u]
            min = u
    return Q.pop(Q.index(min))

def w(u,v,G):
    #print(list(range(0,len(G[u]),2)))
    for i in list(range(0,len(G[u]),2)):
        #print(i)
        if G[u][i]==v:
            return G[u][i+1]
    
    return -1


def relax(u,v,G,d, pi):
    if w(u,v,G)>0:
        if d[u] > d[v] +w(u,v,G):
            d[u]=d[v]+w(u,v,G)
            pi[u]= v


def dijkstra(G,s):
    d,pi=initialize_SS(G,s)
    S=[]
    Q=list(range(len(G)))
    while(Q!=[]):
        u =extract_min(Q,G,d)
        S.append(u)
        for v in S:
            relax(u,v,G,d, pi)
    return d,pi, S, Q


def rutas(pi, i, l):
    l.append(i)
    if pi[i]!= None:
        rutas(pi,pi[i],l)
        
    return l

def todos_nodos(g):
    r =[]
    ds=[]
    for i in range(len(g)):
        nl=[]
        r.append(nl)
        #print(f"padre {i}")
        d,pi, S, Q=dijkstra(g,i)
        for j in range(len(pi)):
            l=[]
            rut =rutas(pi,j,l)
            r[i].append(rut)
        ds.append(d)
    return r,ds

def dibujar(d,pi):
    
    G = nx.DiGraph()
    for j in range(len(d)):
        G.add_node(j, d=d[j])
    
    for i in range(len(pi)):
        if pi[i] != None:
            G.add_edge(pi[i],i)
    #color_map =[color]
    #color_map =[node_color for node in G]
    #nx.draw(G, with_labels=True, node_color=colors, font_color= 'yellow')

    #plt.show()
    return G



if __name__=="__main__":
    G=lg('ejemplo1.txt')
    print(G)
    # r,d=todos_nodos(G)
    # print(f"rutas: {r}")
    # print(f"distancias: {d}")
    d,pi, S, Q=dijkstra(G,5)
    print(d,pi,S,Q)
   

    Gf=dibujar(d,pi)
    nx.draw(Gf, with_labels=True,  arrows=True)
    pos = nx.spring_layout(Gf)
    labels = dict(enumerate(d))
    nx.draw_networkx_labels(Gf,pos,labels)
    plt.show()