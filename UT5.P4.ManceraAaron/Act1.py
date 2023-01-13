'''
Escribir un programa que procese una serie de cadenas introducidas por teclado. 
Sabemos que la carga de datos finaliza cuando el usuario introduzca la cadena “0”. 
Se pide mostrar el total de ocurrencias de cada carácter de todas las cadena procesadas.
'''

#nuestro diccionario de palabras
diccionarioDepalabraes={"Palabras":[]}
palabra=""
#Bucle
while palabra!="0":
    palabra=input("Eintroduce un palabra (0 para finalizar) :")
    #Si escribe 0 se acaba el while
    if palabra == "0":
        break
    #Añadimos la palabra a nuestra key Palabras
    diccionarioDepalabraes["Palabras"].append(palabra)
    #Implementacion de las ocurrencias
    for c in palabra:
        i=0
        #Se mira si ya existe esa key en el diccionario
        if c in diccionarioDepalabraes:
            i=int(diccionarioDepalabraes.get(c))
            diccionarioDepalabraes[c]=str (i+1)
        #Si no existe se implementa
        else:
            diccionarioDepalabraes[c]=str (i+1)
#Muestra por pantalla
print(f"{diccionarioDepalabraes}")
