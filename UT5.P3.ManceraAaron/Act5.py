'''
Diseñar el programa que:
    Cree una tabla (lista con dos dimensiones) de 5x5 enteros.
    Carga la tabla con valores numéricos enteros.
    Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.
'''
listaDimension2=[[1,2,3,4,5],[6,7,8,9,10]]
suma1=0
suma2=0
for i in range(len(listaDimension2)):
    for x in range (len(listaDimension2[i])):
        if(i==0):
            #suma del 1 al 5
            suma1+=listaDimension2[i][x]
        else:
            #suma del 7 al 10
            suma2+=listaDimension2[i][x]
sumaTodo=suma1+suma2
print(f"Suma de la fila 1: {suma1}")
print(f"Suma de la fila 2: {suma2}")
print(f"Suma de todo {sumaTodo}")