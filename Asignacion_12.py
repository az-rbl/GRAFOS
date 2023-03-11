from Asignacion_8_1 import leer_grafo as lg
def initialize_SS(G,s):
    d = [1000]*len(G)
    pi = [None]*len(G)
    d[s]=0
    return d,pi
def extract_min(Q,G,d):
    pass
def relax(u,v,G,d):
    pass

def dijkstra(G,s):
    d,pi=initialize_SS(G,s)
    S=[]
    Q=G
    while(Q!=[]):
        u =extract_min(Q,G,d)
        S.append(u)
        for v in S:
            relax(u,v,G,d)

if __name__=="__main__":
    G=lg('ejemplo1.txt')
    d,pi=initialize_SS(G,0)
    print(d,pi)
    