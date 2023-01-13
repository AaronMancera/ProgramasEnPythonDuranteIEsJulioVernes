'''
Escriba un programa que permita crear una lista de palabras y que, a continuación de las siguientes opciones:
    Contar: Me pide una cadena, y me cuantas veces aparece en la lista
    Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas las apariciones de la primera por la segunda en la lista.
    Eliminar: Me pide una cadena, y la elimina de la lista.
    Mostrar: Muestra la lista de cadenas
    Terminar
'''
listaPalabras = []
palabra = input("Introduce una palabra (- para terminar):")
while palabra != "-":
    listaPalabras.append(palabra)
    palabra = input("Introduce una palabra (- para terminar):")
opcion=0
while opcion!=5:
    print("********************")
    print("* 1. Contar         *")
    print("* 2. Modificar      *")
    print("* 3. Eliminar       *")
    print("* 4. Mostrar        *")
    print("* 5. Salir          *")
    print("********************")
    opcion=int(input("Opcion: "))
    if opcion==1:
        cadena=input("Cadena a buscar: ")
        print(f"La cadena aparece en la lista de palabras {listaPalabras.count(cadena)} veces")
    elif opcion==2:
        cadena=input("Cadena a buscar: ")
        cadena2=input("Cadena a modificar: ")
        i=0
        for palabra in listaPalabras:
            if palabra == cadena:
                listaPalabras[i] = cadena2
            i+=1
    elif opcion==3:
        cadena=input("Cadena a eliminar: ")
        if cadena in listaPalabras:
            for i in range(listaPalabras.count(cadena)):
                listaPalabras.remove(cadena)
        else:
            print("No existe la cadena en la lista de palabras")
    elif opcion==4:
        for palabra in listaPalabras:
            print(palabra)