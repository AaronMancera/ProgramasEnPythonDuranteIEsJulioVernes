import random
'''
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) 
y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado 
y su cubo.
'''
listaAleatorios=[]
for i in range(0,10):
    num=random.randint(1,10)
    listaAleatorios.append(num)
print(f"Los numeros aleatorios ya han sido generada{listaAleatorios}.")
print("Ahora veamos sus cuadrados y cubos:")
cont=1
for x in listaAleatorios:
    print(f"Numero {cont}")
    print(x**2)
    print(x**3)
    cont+=1
