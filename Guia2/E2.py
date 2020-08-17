#Crear una lista con 10 números enteros cualquiera. Indicar cuál es el número mayor y cuál es el número menor.
# Si al menos hay 3 números mayores a 100, imprimir esos números, si no, imprimir los números menores a 50 que formen parte de la lista.

list_numeros = [8, 45, 32, 150, 128, 84, 12, 55, 60, 110]

max_lista = max(list_numeros)
min_lista = min(list_numeros)

print(max_lista)
print(min_lista)

mayores_100 = []
for i in list_numeros:

    if i > 100:
        mayores_100.append(i)
if len(mayores_100) >= 3:
    for numero in mayores_100:
        print(numero)
else:
    for numero in list_numeros:
        if numero < 50:
            print(numero)    
        