from Asignacion_8_1 import leer_grafo as lg
import networkx as nx
import matplotlib.pyplot as plt

def initialize_SS(G,s):
    d = [1000]*len(G)#distancias llenas con infintio
    pi = [None]*len(G)#padres
    d[s]=0#nodo inicial
    return d,pi

#funcion que regresa el valor de peso mínimo de entre los nodos de la cola Q
def extract_min(Q,G,d):
    min_w = 1000
    for u in Q:
        if d[u] < min_w:
            min_w = d[u]
            min = u
    return Q.pop(Q.index(min))

def w(u,v,G):
    #print(list(range(0,len(G[u]),2)))
    for i in list(range(0,len(G[u]),2)):#cuenta de dos en dos en dos
        #print(i)
        #print(f"{G[u][i]}=={v}")
        if G[u][i]==v:
            return G[u][i+1] #regresa el peso
    return 1000
    #return -1


def relax(u,v,G,d, pi):# Calcula el peso hacia de un nodo a otro nodo
    #if w(u,v,G)>0:
    if d[v] > d[u] +w(u,v,G):
        d[v]=d[u]+w(u,v,G)
        pi[v]= u


def dijkstra(G,s):
    d,pi=initialize_SS(G,s)
    S=[] #Cola de los nodos clasificados
    Q=list(range(len(G))) #nodos no clasificados
    while(Q!=[]):# Mientras haya nodos no clasificados
        u =extract_min(Q,G,d) #Extraer el nodo de distancia inima, raiz primero
        S.append(u) #añadirlo a los clasificados,
        for v in Q:
            relax(u,v,G,d, pi) #Va pasar los no clasificados a un relajamiento
        print(d,pi, S, Q)
    return d,pi, S, Q


def rutas(pi, i, l):
    l.append(i)
    if pi[i]!= None:
        rutas(pi,pi[i],l)
        
    return l

def todos_nodos(g):
    r =[]
    ds=[]
    pis= []
    for i in range(len(g)):
        nl=[]
        r.append(nl)
        #print(f"padre {i}")
        d,pi, S, Q=dijkstra(g,i)
        pis.append(pi)
        for j in range(len(pi)):
            l=[]
            rut =rutas(pi,j,l)
            r[i].append(rut)
        ds.append(d)
    return r,ds,pis

def dibujar(d,pi):
    
    G = nx.DiGraph()
    for j in range(len(d)):
        G.add_node((j,d[j]))
    
    for i in range(len(pi)):
        if pi[i] != None:
            G.add_edge((pi[i],d[pi[i]]),(i,d[i]))
    #color_map =[color]
    #color_map =[node_color for node in G]
    #nx.draw(G, with_labels=True, node_color=colors, font_color= 'yellow')

    #plt.show()
    return G

def graficar(ds,pis):
    fig, all_axes = plt.subplots(2, 2)
    ax = all_axes.flat
    for i in range(4):
         nx.draw(dibujar(ds[i],pis[i]), with_labels=True,  arrows=True,node_color='pink', ax=ax[i])
         ax[i].set_title(f"Arbol con origen en {i}")
    plt.show()

if __name__=="__main__":
    G=lg('ejemplo1.txt')
    print(G)
    r,d, pi=todos_nodos(G)
    print(f"rutas: {r}")
    print(f"distancias: {d}")
    # d,pi, S, Q=dijkstra(G,5)
    # print(d,pi,S,Q)
    graficar(d,pi)

    # Gf=dibujar(d,pi)
    # nx.draw(Gf, with_labels=True,  arrows=True,node_color='pink')
    #pos = nx.spring_layout(Gf)
    #labels = dict(enumerate(d))
    #nx.draw_networkx_labels(Gf,pos,labels)
    # plt.show()