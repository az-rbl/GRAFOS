'''
Asignacion_15.py
Implementar algoritmo de Graham parte-2
Raúl Badillo Lora
Completar el cálculo del convex-hull con el algoritmo de Graham 
'''

import Asignacion_14 as ghm1
import networkx as nx
from matplotlib import pyplot as plt

def izq(p1, p2, p3):

    check = ((p2[0] - p1[0]) * (p3[1] - p1[1])) - ((p2[1] - p1[1]) * (p3[0] - p1[0]))

    return False if check < 0 else True 

def Graham(nube):
    
    min,S, Polig, i = ghm1.init_graham(nube)
    i=0
    print(S, Polig)
    while i < len(S):
        t = Polig.pop()
        #print(Polig[-1],t,S[i], Polig)
        if izq(Polig[-1],t,S[i]):
            print(f"la linea que va de {t} a {S[i]} va a la izquierda")
            Polig.append(t)
            Polig.append(S[i])
            i+=1
            
        else:
            print(f"la linea que va de {t} a {S[i]} va a la derecha")
    return Polig

def Graph_graham(nube, graham):
    G = nx.Graph()
    G.add_node(0,pos=graham[0])
    for i in nube:
        G.add_node(nube.index(i)+1,pos=i)
        print(nube.index(i), i)
    G.add_edge(0,nube.index(graham[1])+1)
    for i in range(2,len(graham)):
        G.add_edge(nube.index(graham[i])+1,nube.index(graham[i-1])+1)
    G.add_edge(nube.index(graham[len(graham)-1])+1,0)
    pos = nx.get_node_attributes(G,'pos')
    return G, pos
            
if __name__=='__main__':
    nube = ghm1.random_nube(10)
    print(nube)
    graham =Graham(nube)
    print(graham)
    G, pos = Graph_graham(nube, graham)
    nx.draw(G,pos)
    plt.show()