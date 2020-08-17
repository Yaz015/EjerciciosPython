# Ejercicio 9: Crear un programa que pregunte al usuario 5 números enteros y devuelva una lista con ellos.


n = 0
lista = []

while n < 5:
    numerosEnteros = int(input("Ingrese un número: "))
    lista.append(numerosEnteros)
    n += 1

print(lista)
