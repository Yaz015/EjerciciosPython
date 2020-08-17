# Ejercicio 10: Escribir un programa que almacene todas las letras del abecedario y luego elimine las vocales y nos devuelva una lista sin las vocales, 
# sin modificar la original.


letrasAbc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letrasAbcd= letrasAbc.copy()

for i in letrasAbcd:
    vocales = ["a", "e", "i", "o", "u"]
    for vocal in vocales:
        if i == vocal:
            letrasAbcd.remove(i)
print(letrasAbc)
print(letrasAbcd)        

from string import ascii_lowercase

print(ascii_lowercase)
lista_abc = list(ascii_lowercase)
print(lista_abc)