'''
Programa con menu cuyo objetivo es guardar y alcenar las tiradas de diferentes jugadores
1. Registrar nuevo jugador. Se registra un jugador
2. Buscar jugador. Se busca si existe el jugador y comienza el juego
    1. Tirar dado. lo que sumara en tiradas y lo guarda en un txt con su nombre
    2. Revisa si existe y si es asi lo muestra
    3. Salir
3. Salir
'''
import csv
import random

#len(lista/diccionario/conjunto/tupla)
# if 0 in lista true si existe o false si no
#conjunto={} este es para quitar datos repetidos
#lista=[] .append del(lista[0])
#tupla=() .add .remove(0)
#diccionario={"Key":"atributo","Key2":["atribu1","atribut2"]} diccionario["keyNoExiste"]=0 del(diccionario["keyNoExiste"])
#print(lista * 3) se concatena 3 veces


path="./UT5.PRepaso.CvConDados/datos/dados.csv"
pathTxt="./UT5.PRepaso.CvConDados/datos/"
def menu_registro():
    opcion=0
    while opcion!=3:
        print("1. Registrar nuevo jugador")
        print("2. Acceder con jugador")
        print("3. Salir")
        opcion=int(input("Escribe la opcion: "))
        if opcion==1:
            existe=False
            nombreJugador=input("Escribe el nombre del jugador para registrar: ")
            with open(path,encoding='utf-8') as file:
                #Convierte lo que lea en una lista
                lector = csv.reader(file)
                #Se salta la primera linea que son los nombres de las columnas
                next(lector)
                #Convierte lo que lea en un diccionario
                #lector=csv.DictReader(file)
                for line in lector:
                    #dentro de la lista que ha abstraido debe de ir linea por linea y dentro buscar si el nombre ya existe
                    if nombreJugador in line:
                        existe=True
                        print("Error el usuario ya existe...")
                        break
            if existe==False:
                with open(path,mode='a',encoding='utf-8') as file:
                    file.write(nombreJugador+"\n")
        elif opcion==2:
            existe=False
            nombreJugador=input("Escribe el nombre del jugador al que quieres acceder: ")
            with open(path,encoding='utf-8') as file:
                #Convierte lo que lea en una lista
                lector = csv.reader(file)
                #Se salta la primera linea que son los nombres de las columnas
                next(lector)
                for line in lector:
                    #dentro de la lista que ha abstraido debe de ir linea por linea y dentro buscar si el nombre ya existe
                    if nombreJugador in line:
                        existe=True
                if existe==True:
                    print("Accediendo con exito...")
                    menu_juego(nombreJugador)
                else:
                    print("Error nombre de jugador no encontrado")
        elif opcion==3:
            print("Hasta luego")
                    
def menu_juego(nombreJugador):
    print("Dentro juego como "+nombreJugador)
    opcion=0
    while opcion!=3:
        print("Bienvenido al juego del dado")
        print("1. Tirar")
        print("2. Mirar puntuaciones")
        print("3. Salir")
        opcion=int(input("Escribe la opcion: "))
        if opcion==1:
            dado=random.randint(1,9)
            #Con el mode="a" se añade y con el mode="w" se sobreescribe
            with open(pathTxt+nombreJugador+".txt",mode="a",encoding="utf-8") as file:
                file.write(str(dado)+"\n")
        elif opcion==2:
            try:
                #Sin nada de mode se lee
                with open(pathTxt+nombreJugador+".txt",encoding="utf-8") as file:
                    for linea in file:
                        print(linea+"\n")
            except:
                print("No existe el fichero...")
                
        if opcion==3:
            print("Volviendo al menu anterior")
#Ejecucion del programa
menu_registro()