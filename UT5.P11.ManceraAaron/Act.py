import csv
import random

'''
La Lotería Primitiva es un juego de azar que consiste en elegir 6 números diferentes entre
1 y 49, con el objetivo de acertar la Combinación Ganadora en el sorteo correspondiente

Existen 8 bloques y los números posibles de cada bloque van del 1 al 49.
Cada combinación de 6 números es considerada 1 apuesta sencilla. En un boleto de
papel de La Primitiva hay un total de 8 bloques.
Nosotros vamos a pagar un poco más y en lugar de elegir 6 números, vamos a elegir 8.
Para ganar premios en el Sorteo de La Primitiva, como mínimo deberás acertar 3
números de tu boleto con la combinación ganadora.

ACIERTOS PREMIO
3 100 euros
4 1200 euros
5 30000 euros
6 400000 euros

La aplicación consiste en crear una aplicación en Python. Se aporta un archivo csv que
posee la siguiente estructura:
Nombre:Apellido:Num1:Num2:Num3:Num4:Num5:Num6:Num7:Num8
Una misma persona puede jugar más de una apuesta.
Si necesitas modificar el csv incrementando alguna columna, puedes hacerlo

El ejercicio debe mostrar un menú:
1. Mostrar todos los jugadores y sus apuestas con un aspecto bonito
2. El programa podrá:
a. genera la combinación ganadora aleatoriamente.
b. Dejar que yo escriba una
Se mostrará
La combinación ganadora de hoy es: ….
3. Insertar un nuevo jugador con su combinación
4. Comprobar quién ha acertado 3 aciertos y mostrarlo
5. Comprobar quién ha acertado 4 aciertos y mostrarlo
6. Comprobar quién ha acertado 5 aciertos y mostrarlo
7. Comprobar quién ha acertado 6 aciertos y mostrarlo
8. Salir

En el caso que no acierte mostrará: “No hay nadie con aciertos”
'''
path="./UT5.P11.ManceraAaron/datos/jugadores-loteria.csv"
numeroGanador=-1
numerosGanadores=[]
def mostrarTodosLosParticipantes():
    print()
    print("Mostrando los participantes")
    with open(path,encoding='utf-8') as file:
        lector = csv.reader(file)
        next(lector)
        for line in lector:
            for palabra in line:
                segmentado=palabra.split(":")
                print(segmentado)
    print()

def combinacionGanadora():
    print("1. Genera la combinación ganadora aleatoriamente.")
    print("2. Dejar que yo escribir manualmente.")
    combi=int(input("Opcion: "))
    if combi==1:
        print()
        for i in range(6):
            numeroGanador=random.randint(1,49)
            numerosGanadores.append(numeroGanador)
        print(numerosGanadores)
    elif combi==2:
        print()
        for i in range(6):
            numeroGanador=int(input("Introduce el numero ganador: "))
            numerosGanadores.append(numeroGanador)
        print(numerosGanadores)
    else:
        print("Error, vuelva a intentarlo...")
    print()

def insertarNuevoJugador():
    print()
    with open(path,mode='a',encoding='utf-8') as file:
        nuevoJugadorNombre=input("Introduce el nombre: ")
        nuevoJugadorApellido=input("Introduce el apellido: ")
        nuevoJugadorBoleto1=input("Introduce el boleto1: ")
        nuevoJugadorBoleto2=input("Introduce el boleto2: ")
        nuevoJugadorBoleto3=input("Introduce el boleto3: ")
        nuevoJugadorBoleto4=input("Introduce el boleto4: ")
        nuevoJugadorBoleto5=input("Introduce el boleto5: ")
        nuevoJugadorBoleto6=input("Introduce el boleto6: ")
        nuevoJugadorBoleto7=input("Introduce el boleto7: ")
        nuevoJugadorBoleto8=input("Introduce el boleto8: ")
        file.write(nuevoJugadorNombre+":"+nuevoJugadorApellido+":"+nuevoJugadorBoleto1+":"+nuevoJugadorBoleto2+":"+nuevoJugadorBoleto3+":"+nuevoJugadorBoleto4+":"+nuevoJugadorBoleto5+":"+nuevoJugadorBoleto6+":"+nuevoJugadorBoleto7+":"+nuevoJugadorBoleto8+"\n")

def comprobarAcierto3():
    print()
    print("Mostrando los participantes ganadores de 3 aciertos")
    with open(path,encoding='utf-8') as file:
        lector = csv.reader(file)
        next(lector)
        for line in lector:
            cont=0
            #print(line)
            for palabra in line:
                segmentado=palabra.split(":")
                for i in range(2,10,1):
                    #print("Segmento:"+segmentado[i])
                    for j in numerosGanadores:
                        #print("numeroGanador "+str(j))
                        if int(segmentado[i])==int(j):
                            cont=cont+1
                        
                #print(cont)
                if cont==3:
                    print(segmentado[0]+" "+segmentado[1]+" ha ganado 100")


def comprobarAcierto4():
    print()
    print("Mostrando los participantes ganadores de 4 aciertos")
    with open(path,encoding='utf-8') as file:
        lector = csv.reader(file)
        next(lector)
        for line in lector:
            cont=0
            #print(line)
            for palabra in line:
                segmentado=palabra.split(":")
                for i in range(2,10,1):
                    #print("Segmento:"+segmentado[i])
                    for j in numerosGanadores:
                        #print("numeroGanador "+str(j))
                        if int(segmentado[i])==int(j):
                            cont=cont+1
                        
                #print(cont)
                if cont==4:
                    print(segmentado[0]+" "+segmentado[1]+" ha ganado 1200")

def comprobarAcierto5():
    print()
    print("Mostrando los participantes ganadores de 5 aciertos")
    with open(path,encoding='utf-8') as file:
        lector = csv.reader(file)
        next(lector)
        for line in lector:
            cont=0
            #print(line)
            for palabra in line:
                segmentado=palabra.split(":")
                for i in range(2,10,1):
                    #print("Segmento:"+segmentado[i])
                    for j in numerosGanadores:
                        #print("numeroGanador "+str(j))
                        if int(segmentado[i])==int(j):
                            cont=cont+1
                        
                #print(cont)
                if cont==5:
                    print(segmentado[0]+" "+segmentado[1]+" ha ganado 30000")

def comprobarAcierto6():
    print()
    print("Mostrando los participantes ganadores de 6 aciertos")
    with open(path,encoding='utf-8') as file:
        lector = csv.reader(file)
        next(lector)
        for line in lector:
            cont=0
            #print(line)
            for palabra in line:
                segmentado=palabra.split(":")
                for i in range(2,10,1):
                    #print("Segmento:"+segmentado[i])
                    for j in numerosGanadores:
                        #print("numeroGanador "+str(j))
                        if int(segmentado[i])==int(j):
                            cont=cont+1
                        
                #print(cont)
                if cont==6:
                    print(segmentado[0]+" "+segmentado[1]+" ha ganado 400000")


opcion=0
while opcion!=8:
    print("-------------------------------------------------------------")
    print(" 1. Participantes")
    print(" 2. Combinacion ganadora")
    print(" 3. Insertar nuevo")
    print(" 4. Comprobar quién ha acertado 3 aciertos y mostrarlo")
    print(" 5. Comprobar quién ha acertado 4 aciertos y mostrarlo")
    print(" 6. Comprobar quién ha acertado 5 aciertos y mostrarlo")
    print(" 7. Comprobar quién ha acertado 6 aciertos y mostrarlo")
    print(" 8. Salir")
    print("-------------------------------------------------------------")
    opcion=int(input("Escribe la opcion (1-8): "))
    if opcion<1 and opcion>8:
        print("Opcion introducida erronia...")
    elif opcion==1:
        mostrarTodosLosParticipantes()
    elif opcion==2:
        combinacionGanadora()
    elif opcion==3:
        insertarNuevoJugador()
    elif opcion==4:
        comprobarAcierto3()
    elif opcion==5:
        comprobarAcierto4()
    elif opcion==6:
        comprobarAcierto5()
    elif opcion==7:
        comprobarAcierto6()
    elif opcion==8:
        print("Adios...")