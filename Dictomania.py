import math
""" El input de este codigo te tienes en verde si quieres escribir tu propia lista y valor que quieres encontrar
Pero ahorra tienes un ejemplo de como seria el input """
# dictionario=input('Escribe tu lista: ').split()
# dictionario = list(map(int, dictionario))
# valores=int(input('Escribe un numero del dicionario creado: '))
dictionario = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 10, 12, 13, 14, 15, 16, 20, 70, 80, 19]
dictionario.sort()  # esto es para ordenar la lista si escribes en desorden
valores = 13 

""" Estas funciones nos ayudan a buscar el numero esto lo hace mirando las condiciones de la funcion busca.
Que se va acercando a la position de los valores.
Si la izq > der significa que el vaor no existe."""
def dicotomía(valores, dictionario):
    def busca(izq, der):#izquierda derecha respectivamente
        if izq > der:
            return -1 
        mediana_int = (izq + der) // 2
        if dictionario[mediana_int] == valores:
            return mediana_int
        elif dictionario[mediana_int] > valores:
            return busca(izq, mediana_int - 1)
        else:
            return busca(mediana_int + 1, der)  

    return busca(0, len(dictionario) - 1)#buscar quitando la ultima parte de la lista

""" El output comprueba primero si el valor que estamos buscando esta en el dicionario o esta fuera de el
Por eso ponemos las dos condiciones (position -1 significa que esta fuera de la tabla) """
position = dicotomía(valores, dictionario)

if position != -1:
    print("El valor {} se encuentra en la posición {}.".format(valores, position))#esta en la tabla esto es porque no es un valor fuera de la izq o der
else:
    print("El valor {} no se encuentra en la tabla; position {} ".format(valores,position))
