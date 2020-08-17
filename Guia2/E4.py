#Ingresar 6 números por teclado, preferentemente enteros, ordenarlos de manera creciente e imprimirlos por pantalla.


list_numeros_enteros = []

for i in range(6):
    numeros_enteros = int(input("Ingrese un numero: "))
    list_numeros_enteros.append(numeros_enteros)
    list_numeros_enteros.sort()

print(list_numeros_enteros)