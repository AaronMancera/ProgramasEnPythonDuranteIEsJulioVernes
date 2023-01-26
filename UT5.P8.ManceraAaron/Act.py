'''
Dado el fichero estaciones.csv crea un programa que trabaje con el fichero, 
extraiga información, la muestra, … 

Todo el programa debe estar comentado. 

NINGÚN PROGRAMA ES “PARECIDO” AL DE OTRO COMPAÑERO/A

Se debe entregar zip con : 
Enunciado descriptivo como si fuera una tarea
Programa

'''
path="./UT5.P7.ManceraAaron/datos/estaciones.csv"
print("-------- Bienvenido al programa GESTION DE ESTACIONES --------")
print("Cargando fichero....")
with open(path,encoding='utf-8') as file:
    