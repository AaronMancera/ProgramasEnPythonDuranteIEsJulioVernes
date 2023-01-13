import random
'''
    Hacer un programa que inicialice una lista de números 
    con valores aleatorios (10 valores),
    y posterior ordene los elementos de menor a mayor.
'''
listaAleatorios=[]
for i in range(0,10):
    num=random.randint(1,10)
    listaAleatorios.append(num)
print(f"Lista desordenada: {listaAleatorios}")
listaAleatorios.sort(key=abs)
print(f"Lista ordenada de menor a mayor: {listaAleatorios}")