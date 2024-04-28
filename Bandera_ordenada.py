import os
import time
import random

#El input del algoritmo puedes poner las veces que quieras los colores escritos en la consola
color=input('escribe el orden que estan los colores \nrojo verde y azul:\n').lower().split()
color = list(map(str, color))#lo crea para que sea una lista
""" Esta funcion del algoritmo mezcla los colores para que esten desorganizados """
def bandera(color):
    random.shuffle(color)
    return color
#Ahora lo que tenemos como color es los colores mezclados
color=bandera(color)
print(color)
time.sleep(2)
os.system('cls')
""" La funcion ordenar del algoritmo ordena los colores escritos en el input en el siguiente orden:
Rojo verde y azul.
Para conseguir esto se multiplica los colores ya ordenados con las veces que estaban escritos
en el input anterior """
def ordenar(color):
    #principio es 0
    rojo= 0
    verde= 0
    azul= 0
    # Recorrer la secuencia una sola vez para contar los colores que hay
    for tipo in color:
        if tipo == "rojo":
            rojo += 1
        elif tipo == "verde":
            verde += 1
        elif tipo == "azul":
            azul += 1

    ordenado = (["rojo"] * rojo) + (["verde"] * verde) + (["azul"] * azul)
    #multiplicamos los colores por cuantos rojos verdes y azules que hay
    
    return ordenado

#El output del progrma te devuelve los colores el el orden deseado
ordenada = ordenar(color)
print("Bandera de Dijkstra:\n", ordenada)

        
