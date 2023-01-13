'''
Modifica el ejercicio anterior para que el programa informe del número de ocurrencias de 
las distintas letras del alfabeto incluyendo aquellas que no aparezcan (indicar valor 0)

'''
#tupla de todo el abecedario
tuplaAbecedario=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z")
#nuestro diccionario de palabras
diccionarioDepalabraes={"Palabras":[]}
palabra=""
#Creamos en el diccionario las key de las letras para luego registrar las ocurrencias
for a in tuplaAbecedario:
    diccionarioDepalabraes[a]="0"
#Bucle
while palabra!="0":
    palabra=input("Eintroduce un palabra (0 para finalizar) :")
    #Si escribe 0 se acaba el while
    if palabra == "0":
        break
    #Añadimos la palabra a nuestra key Palabras
    diccionarioDepalabraes["Palabras"].append(palabra)
    #Implementacion de las ocurrencias
    for l in tuplaAbecedario:
        for c in palabra:
            if l==c:
                i=0
                i=int(diccionarioDepalabraes.get(l))
                diccionarioDepalabraes[c]=str (i+1)
#Muestra por pantalla
print(f"{diccionarioDepalabraes}")