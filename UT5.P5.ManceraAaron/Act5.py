import random

'''
Crea una función calcularMaxMin que recibe una serie de valores numéricos 
y devuelve el valor máximo y el mínimo. 
Crea un programa que genere x números aleatorios en el intervalo [1,100] 
y muestre el máximo y el mínimo utilizando la función anterior.
'''
def calcularMaxMin (numeros):
    max=0
    min=101
    for num in numeros:
        if num>max:
            max=num
        elif num<min:
            min=num
    print(f"El máximo es: {max}")
    print(f"El mínimo es: {min}")

numeros=[]
x=input("Escribe cuantos numeros vas a generar: ")
for i in range (1,int(x),+1):
        numeros.append(random.randint(1,100))
calcularMaxMin(numeros)
#Para comprobar
#print(numeros)