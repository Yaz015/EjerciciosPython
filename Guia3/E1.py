# Crear una función que, a partir de un dato de entrada que sea en horas, 
# nos informe cuántos minutos y cuántos segundos serían esas horas. Imprimir por pantalla dichos valores.

hora = int(input("Ingresar hora: "))

minutos = hora * 60 
segundos = hora * 3600

print (f"La hora seleccionada es: {minutos, segundos }")