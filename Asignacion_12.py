def initialize_SS(G,s):
    d = [1000]*len(G)
    pi = [None]*len(G)
    d[s]=0
    return d,pi
def extract_min(q):
    pass
def relax(u,v,w):
    pass

def dijkstra(G,w,s):
    d,g=initialize_SS(G,s)
    S=[]
    Q=G
    while(Q!=[]):
        u =extract_min(Q)
        S=u
        for v in S:
            relax(u,v,w)
    