#Crear un diccionario con 5 estudiantes y sus respectivas notas. Imprimir por pantalla los alumnos que aprobaron y su nota 
# (no en forma de diccionario, si no con nombre : nota). Tener en cuenta que para aprobar el alumno debe sacarse una nota mayor o igual a 7 y menor o igual a 10.

estudiantes = {"Gonzales Pablo" : 3, "Alvarez Laura": 8, "Garcia Stephanie" : 6, "Perez Juan" : 9, "Martinez Andres" : 4}

list_notas = list(estudiantes.values())
list_nombres = list(estudiantes.keys())



for nombres, notas in estudiantes.items():
    if notas >= 7:
        print(f"{nombres} : {notas}")