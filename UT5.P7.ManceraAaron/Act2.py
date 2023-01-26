import os
'''
Implementar un programa que permita realizar la operación de copia de un fichero. 
Tanto origen.txt como destino.txt serán ficheros de texto cuyos nombres 
indicará el usuario por teclado.

Se debe utilizar readline() para la lectura del fichero origen y comprobar su existencia 
con os.path.isfile ()
'''
nombreOrigen=input('Escribe el nombre del archivo origen (recurda introducir el .txt): ')
nombreCopia=input('Escribe el nombre de la copia (recurda introducir el .txt): ')
pathOrigen="./UT5.P7.ManceraAaron/ficheros/"+nombreOrigen
if(os.path.isfile(pathOrigen)):
    pathDestino="./UT5.P7.ManceraAaron/ficheros/"+nombreCopia
    print("Realizando copia del fichero...")
    with open(pathOrigen, encoding='utf-8') as fOrigen:
        with open(pathDestino, mode='w', encoding='utf-8') as fDestino:
            for linea in fOrigen:
                fDestino.write(str(linea))
print("Copia del origen realizada...")
