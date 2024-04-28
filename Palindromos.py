
""" La clase palindromo esta creada por un solo atributo que es la palabra.
La clase tiene tres funciones muy importantes:
La esalphanumereco comprueba si la palabra esta compuesta o de numeros o letras del abcedario
Luego tenemos la esPalindromo que es la que comprueba que toda la palabra esta en minuscula y que sus acentos se vayan
La del resultado te da si es palindrom o no en formato string

Finalmente creamos un decorado __str__ para devorver el resultado

"""
class Palindromos:

    def __init__(self, palabras):
        self.palabras = palabras

    def esalphanumerico(self):
        abc= str.ascii_letters + "áéíóúüñÁÉÍÓÚÜÑ"
        if self.palabras is abc or int:
            return self.palabras
        else:
            raise ValueError('No es ni numerico ni alphabetico')
    def esPalindromo(self):
        palabras = self.palabras.lower().replace(' ', '').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ü', 'u')
        return palabras == palabras[::-1]

    def resultado(self):
        if self.esPalindromo():
            return f'La palabra {self.palabras} es un palíndromo'
        else:
            return f'La palabra {self.palabras} no es un palíndromo'

    def __str__(self):
        return self.resultado()

def main():
    #El input del algoritmo es simple tienes que escribir la palabra
    palabra = input('Escribe una palabra: ').lower()
    palindromo = Palindromos(palabra)
    #Luego el output te devuelve si es o no palindromo
    print(palindromo)

if __name__ == "__main__":
    main()