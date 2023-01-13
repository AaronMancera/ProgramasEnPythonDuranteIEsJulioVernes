'''
Programa que pida números hasta que se introduzca el 0. 
Debe calcular la suma y la media de los números introducidos.
'''
contador=0
numero=-1
suma=0
while(numero!=0):
    numero=float(input("Introduzca un numero (Si pones 0 se acabo el programa): "))
    if(numero!=0):
        suma+=numero
        contador+=1
print(contador)
print(f"La suma total es {suma}")
print(f"La media total es {suma/contador}")