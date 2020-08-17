#Escribir un programa que seleccione una operación de cuatro operaciones numéricas disponibles,
# una vez seleccionada la operación, introducir dos números y ejecutar la operación.

elegir_operacion = int(input("""Seleccionar la operación que desea realizar:
    1 - Suma
    2 - Resta
    3 - Producto
    4 - División
    Opcion: """ ))
numero1 = int(input("Elegir un numero: "))
numero2 = int(input("Elegir otro numero: "))

if elegir_operacion == 1:
    print(numero1 + numero2)
elif elegir_operacion == 2:
    print(numero1 - numero2)
elif elegir_operacion == 4:
    print(numero1 / numero2)
else:
    print(numero1 * numero2)

