#Asignacion_8_1.py
#Asignación_#8_. 
#Lectura de grafos desde archivos de texto hacia un arreglo de listas ligadas
#Recuperar sus programas en dode ya se implemento la lectura de la conectividad de un grafo desde un archivo de texto hacia una una estructura de datos como una lista de lista o vectores, etc.
#Además de la lectura se deberán declarar e inicializar las estructuras de datos necesarias para la implementación del algoritmo de BFS.
def leer_grafo(string):
    f= open(string,'r')
    s= f.read()
    data = [list(int(x) for x in y.split(' ')) for y in s.split('\n')]
    del data[0]
    # for i in range(len(data)):
    #     for j in range(0,len(data[i]),2):
    #         if data[i][j]!=0:
    #             data[i][j]=1
    return(data)

if __name__=="__main__":
    print(leer_grafo('ejemplo3.txt'))