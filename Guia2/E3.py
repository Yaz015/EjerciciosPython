#Pedir al usuario que ingrese por teclado 2 números, si el primero es menor que el segundo imprimir la resta entre el segundo 
# y el primero, si el primero es mayor que el segundo imprimir la suma de ambos, y si son iguales imprimir su producto.

numero1= int(input("Ingrese un numero: "))
numero2= int(input("Ingrese otro numero: "))

if numero1 < numero2:
    print(numero2 - numero1)
elif numero1 > numero2:
    print(numero1 + numero2)
elif numero1 == numero2:
    print(numero1*numero2)        