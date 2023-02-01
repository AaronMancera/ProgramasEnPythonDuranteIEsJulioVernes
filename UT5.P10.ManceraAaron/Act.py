'''
Realiza una función que reciba un array bidimensional (de longitud variable) un escenario de Buscaminas, 
donde haya un 0 donde no hay minas y un -1 donde si hay.

Para cada casilla que no tenga una mina, diga cuantas minas adyacentes hay en diagonal, 
horizontal y vertical.

Internamente el programa realizará las acciones con una función definida como
def contandoMinas(campo):
La función devolverá un array bidimensional con el número de minas adyacentes en cada posición.

'''

def contandoMina(campo):
    #Guardo la variable de numero de filas
    filas = len(campo)
    #print(filas)
    #Guardo la variable de numero de columna
    columnas = len(campo[0])
    #print(columnas)
    #Se crea un array con las mismas dimensiones escritas con 0 todos sus espacios y esta sera la resultante dle estudio del buscaminas
    resultado = [[0 for a in range(columnas)] for b in range(filas)]
    #print(resultado)
    
    for x in range (filas):
        for y in range (columnas):
            #Si de por si tenia una mina se le pone la mina
            if campo[x][y] == -1:
                resultado[x][y]= -1
                continue
            #A continuacion de saber que tiene mina se estudia cuantas casillas tiene esta bomba alrededor
            for bombasX in range(-1,2):
                for bombasY in range(-1,2):
                    fila=x+bombasX
                    columna=y+bombasY
                    if fila>=0 and fila<filas and columna>=0 and columna<columnas and campo[fila][columna]==-1:
                        resultado[x][y]+=1
                        #print(resultado[x][y])
    return resultado

linea1=[]
linea2=[]
#Se escribe las caracteristicas del campo
print("Bienvenido al buscaminas 2x4")
print("Primera linea")
for i in range(4):
    teclado=int(input("Escribe 0, no hay mina o -1, hay mina: "))
    linea1.append(teclado)
print("Segunda linea")
for i in range(4):
    teclado=int(input("Escribe 0, no hay mina o -1, hay mina: "))
    linea2.append(teclado)
#Se asigna el campo en la terminal
campo=[]
campo.append(linea1)
campo.append(linea2)
print("Mapa de entrada: ")
print(campo)
print("Mapa resultado: ")
print(contandoMina(campo))