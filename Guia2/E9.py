#Pedirle al usuario que ingrese el monto disponible en su tarjeta de crédito. Evaluar si puede realizar una compra de $2500, 
# si puede indicar cuánto saldo le queda luego de efectuarla. Si no puede, indicar cuánto dinero le falta para poder realizarla.

monto_disponible = int(input("Ingrese el monto disponible: "))
compra = 2500

if monto_disponible >= compra:
    print(f"Su compra se ha realizado con exito. Su monto actual es: {monto_disponible - compra} ")
else:
    print(f"Le falta para realizar la compra: {compra - monto_disponible}")