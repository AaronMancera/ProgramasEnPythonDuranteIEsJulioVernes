'''
Escribir un programa que pida al usuario 
un número entero y muestre por pantalla 
un triángulo rectángulo como el de más abajo, 
de altura el número introducido.
'''
numero=int(input("Introduce un numero para formar un triangulo rectangulo: "))
i=numero
cont=0
text=""
for i in range(0,numero):
    text=""
    cont=i
    while(cont!=-1):
        text+="*"
        cont-=1
    print(text)
