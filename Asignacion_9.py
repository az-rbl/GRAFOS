#Asignación_#9. 
# #Implementar el algortitmo de BFS parte1
# Tomar como base la presentación del algoritmo que se hizo en clase e implementar BFS.
# La asignación consiste en leer el grafo desde el archivo de texto, almacenarlo en una estructura de listas de listas e inicializar todas las estructuras de datos necesarias.
from Asignacion_8_1 import leer_grafo as lg

def init_BFS(G,s):
    d =[x for x in range(len(G))]
    pi =[x for x in range(len(G))]
    colors =[x for x in range(len(G))]
    q = [s-1]
    for u in range(len(G)):
        if u !=(s-1):
            colors[u] = 'white'
            d[u] =10000
            pi[u] = None
    colors[s-1]='gray'
    d[s-1] = 0
    pi[s-1] = None
    return colors,d,pi,q
if __name__=="__main__":
    g =lg('ejemplo1.txt')
    print(g)
    print(init_BFS(g,4))
    