'''
Asignacion_14.py
Implementar algoritmo de Graham parte-1
Raúl Badillo Lora
Implementar el algoritmo que se presento en clase para calcular la envoltura convexa de un conjunto de n-puntos en dos dimensiones.
Los n- puntos se pueden generar de forma aleatoria, en esta asignación solo se implementará el proceso de inicialización para verificar que todo esta bien calculado.
'''
import random
import math


def random_nube(size, begin=0, end=10):
    #Genera una nube aleatoria de tuplas de numeros
    nube = [(random.randint(begin,end),random.randint(begin,end))for x in range (size)]
    return nube

def punto_menor(nube): 
    #Obtiene el numero con menor valor de y, en caso de empate, se toma el que tenga x menor
    menor =(float('inf'),float('inf'))
    for i in nube:
        if i[1] < menor[1]:
            menor = i
        elif i[1] == menor[1] and i[0] < menor[0]:
            menor = i
    return nube.pop(nube.index(menor)) 

def AnguloPuntos(p0,p1):
    #regresa el angulo entre dos puntos
    return(math.atan2((p1[1]-p0[1]),(p1[0]-p0[0])))

def OrdenarAngularmente(nube,min):
    #Ordena todos los puntos con respecto a su angulo con el punto menor
    Ordenados = [[min,0]]
    for i in nube:
        Ordenados.append([i,AnguloPuntos(min,i)])
    Ordenados.sort(key= lambda x:x[1])
    lista =[]
    for i in Ordenados:
        i.pop(-1)
        lista.append(i[0])
    return lista
    

def init_graham(nube):
    #Inicialización para el algoritmo de Graham
    min = punto_menor(nube)
    S = OrdenarAngularmente(nube, min)
    Polig =[S.pop(0),S.pop(0),S.pop(0)]
    i = 3
    return  min,S, Polig, i

if __name__=='__main__':
    nube = random_nube(10)
    print(nube)
    #min = punto_menor(nube)
    #print(min)
    print(init_graham(nube))