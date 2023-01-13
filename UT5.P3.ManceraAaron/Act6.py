'''
Crear un programa que añada números a una lista hasta que introducimos un número negativo. 
A continuación debe crear una nueva lista igual que la anterior pero eliminando los números duplicados. 
Muestra esta segunda lista para comprobar que hemos eliminado los duplicados.
'''
lista=[]
listaBuena=[]
num=int(input("Numero (Numero negativo terminan el programa): "))

while num>0:
    lista.append(num)
    num=int(input("Numero (Numero negativo terminan el programa): "))

for i in lista:
    #si no esta en la lista lo incluye
    if i not in listaBuena:
        listaBuena.append(i)
print(listaBuena)