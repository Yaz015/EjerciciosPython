#Crear un diccionario con los meses del año de la forma { 1: "enero"}. Desafío: lograr cambiar las claves. 
#Pista: si imprimen ítems del diccionario les crea una lista. Una vez que lo logren, imprimir el diccionario modificado

meses = { 1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio", 13: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}

list_meses = list(meses.values())
list_numero = list(meses.keys())

meses1 = dict(zip(list_meses, list_numero))

print(meses1)

