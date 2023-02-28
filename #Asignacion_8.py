#Asignacion_8.py
#Grafos 1
#  La asignación consiste en implementar la siguientes confesionalidades para grafos.
# 1. Leer u grafo desde teclado, es decir, capturar la conectividad de alguno de los ejemplos de grafos que se han revisado.
# 2. Mandar a pantalla la matriz de conectividad del grafo para verificar la captura.
# 3. Verificar si el grafo es reflexivo, es decir si existen todas las conexiones de la forma a(i,i)
# 4. Calcular la multiplicación matricial de AxA
# 5. Implementar una función para calcular la potencia n de la matriz A, utilizando la función desarrollada en el punto 4. 

import numpy as np
A = (1, 2, 3, 4)
R = [ (1, 2), (2, 2), (2, 3), (3, 4), (4, 3) ]
#T =[]
def Matriz_conect(A,R):
    Mat = np.empty([len(A), len(A)],dtype=int)
    #print(Mat)
    k=0
    for i in A:
        T=[]
        for j in A:
            t = (i,j)
            if t in R:
                T.append(1)
            else:
                T.append(0)
        #print(Mat[k])
        Mat[k]=T
        k+=1
    return(Mat)

if __name__=='__main__':
    rango=int(input("Cuantos nodos tiene el grafo? "))
    A = list(range(1,rango+1))
    s = input("Relaciones del grafo: ")
    R= [tuple(int(x) for x in y.split(',')) for y in s.split(' ')]
    print(A)
    print(R)
    MC=Matriz_conect(A,R)
    print(MC)
    print(np.multiply(MC,MC))
