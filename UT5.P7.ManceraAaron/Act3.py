'''
Escribir una función, obtenerNumerosArchivo, que reciba por parámetro el nombre de un archivo
que almacenará una serie de cantidades enteras y positivas (un número por línea). 
La función leerá todos los valores del archivo, calculará su suma y la devolverá.
'''
pathNumeros="./UT5.P7.ManceraAaron/ficheros/numerosSumar.txt"
suma=0
with open(pathNumeros,encoding='utf-8') as file:
    print("Realizando la suma...")
    for linea in file:
        suma=int(linea) + suma
print(suma)