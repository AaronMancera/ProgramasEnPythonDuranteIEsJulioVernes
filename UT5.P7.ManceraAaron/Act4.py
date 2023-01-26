'''
Escriba un programa que se encargue de clasificar una serie de cadenas atendiendo a su 
longitud. Se solicitará al usuario el nombre del archivo que contendrá el conjunto de palabras, 
cada una en una línea. También se pedirá por teclado un valor entero que se utilizará como valor 
de corte para clasificar las palabras del archivo anterior. Las palabras con longitud menor al
valor de corte se almacenarán en el fichero menor.txt y el resto de palabras en el fichero mayor.txt
'''
pathOrigen="./UT5.P7.ManceraAaron/ficheros/palabras.txt"
pathMenor="./UT5.P7.ManceraAaron/ficheros/menor.txt"
pathMayor="./UT5.P7.ManceraAaron/ficheros/mayor.txt"
numeroDeCorte=int(input("Escribe el numero que se va a usar de referente como de corte: "))
with open(pathOrigen,encoding='utf-8') as fOrigen:
    with open(pathMenor, mode='w',encoding='utf-8') as fMenor:
        with open(pathMayor,mode='w',encoding='utf-8') as fMayor:
            for linea in fOrigen:
                if (len(linea)-1) < numeroDeCorte:
                    fMenor.write(linea)
                elif (len(linea)-1) >= numeroDeCorte:
                    fMayor.write(linea)
print("Finalizacion del estudio de caracteres...")