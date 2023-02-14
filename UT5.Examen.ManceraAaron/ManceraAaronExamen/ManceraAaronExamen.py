'''
El juego del ahorcado es un juego de adivinar palabras o frases. En este caso serán
palabras.
Las palabras a acertar se generarán aleatoriamente y serán seleccionadas de un fichero que
cada alumno creará. Las palabras serán de 5 , 6 o 7 letras. El fichero debe contener mínimo
20 palabras.
Se debe crear un programa en Python que adivine la palabra con un máximo de 6 intentos.
El jugador debe tratar de acertar en el menor número de intentos posibles.
APARTADOS:
1º Genera la palabra aleatoriamente y mostrará las posiciones.
Ejemplo: imaginemos que es de 5 letras
Inicio juego:
_ _ _ _ _
2º Aparecerán las posiciones de las letras y solicitará una palabra al jugador . Se validará
que introduzca palabras y no números ni espacios vacíos.
3º Mostrará las letras acertadas en la posición que corresponda y debajo indicará las letras
que no están en su posición y las que no están.
4º Solicitará palabras hasta que se acierte o se pierda. Mostrando el mensaje
correspondiente:
Has acertado en 3 intentos ( o el nº que sea)
Has perdido. La palabra correcta era: XXXXX
'''
import random
#Esta es la ruta relativa donde se va a 
path="./data/palabras.txt"
def eleccionPalabra():
    with open(path,encoding="utf-8") as file:
        palabras=[]
        for linea in file:
            palabras.append(linea)
            #print(linea)
    palabrasElegida=palabras[random.randint(0,len(palabras)-1)].replace("\n", "")
    return palabrasElegida

def inicioJuego(palabra):
    cadena=[]
    for i in range(len(palabra)):
        cadena.append("_")
    return cadena

def juego(letra):
    if letra in palabraResolver:
        #print(letra in palabraResolver)
        for i in range(len(palabraResolver)):
            if palabraResolver[i]==letra:
                escenario[i]=letra
        return True
    else:
        return False

def ahorcado(vidas):
    if vidas==6:
        print("================")
        print(" +----+")
        print(" |    |")
        print("      |")
        print("      |")
        print("      |")
    elif vidas==5:
        print("================")
        print(" +----+")
        print(" |    |")
        print(" o    |")
        print("      |")
        print("      |")
    elif vidas==4:
        print("================")
        print(" +----+")
        print(" |    |")
        print(" o    |")
        print(" |    |")
        print("      |")
    elif vidas==3:
        print("================")
        print(" +----+")
        print(" |    |")
        print(" o    |")
        print("/|    |")
        print("      |")
    elif vidas==2:
        print("================")
        print(" +----+")
        print(" |    |")
        print(" o    |")
        print("/|\   |")
        print("      |")
    elif vidas==1:
        print("================")
        print(" +----+")
        print(" |    |")
        print(" o    |")
        print("/|\   |")
        print("/     |")
    elif vidas==0:
        print("================")
        print(" +----+")
        print(" |    |")
        print(" o    |")
        print("/|\   |")
        print("/ \   |")
    
fin=False
letrasEscritas=[]
vidas=6
intentos=0
print("BIENVENIDO AL A-A-A-A-AHORCADO DEFINITIVO")
print("Primero: El programa va a elegir la palabra para resolver")
palabraResolver=eleccionPalabra()
#print(palabraResolver)
print("Segundo: Empieza el juego")
escenario=inicioJuego(palabraResolver)
ahorcado(vidas)
print(escenario)
while fin!=True:
    intentos+=1
    usuario=input("Escribe una letra: ")
    if usuario in letrasEscritas:
        print("No debes de repetir")
    else:
        letrasEscritas.append(usuario)
        if(juego(usuario)==False):
            vidas-=1
        ahorcado(vidas)
        print(escenario)
        print("-----Palabras ya utilizadas-----")
        print(letrasEscritas)
        
        if(vidas==0):
            print("Perdiste... la palabra correcta era: "+palabraResolver)
            break
        if "_" not in escenario:
            print("VICTORIAAAAA!!! Has acertado en "+str(intentos)+" intentos WOOOOOOOOOOW!!!!")
            break
