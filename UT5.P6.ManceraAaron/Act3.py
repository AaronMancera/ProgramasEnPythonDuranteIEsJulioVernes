'''
Escribe un programa en Python que permita guardar las 
notas de un alumno conseguidas en sus distintas asignaturas en una evaluación. 
Guarda la información en un diccionario cuyas claves sean las asignaturas 
y los valores las notas de cada asignatura. Se pide las siguientes funcionalidades:

Introducción de los datos.
Visualización de datos.
Generar medias por asignaturas
Generar la nota media final del alumno
'''
dicNot = {}

# Introducción de los datos. Se introduce el numero de asignaturas y las notas que han conseguido en ella
num_asignaturas = int(input("Introduce el número de asignaturas: "))
for i in range(num_asignaturas):
    asignatura = input("Introduce el nombre de la asignatura: ")
    while asignatura in dicNot:
        print("Error, has introducindo una asignatura que ya existe")
        asignatura = input("Introduce el nombre de la asignatura: ")
    nota=1
    listNotas=[]
    while nota >=0:
        nota = float(input("Introduce la nota de la asignatura (escribe num negativo para finalizar): "))
        if(nota>=0):
            listNotas.append(nota)
    dicNot[asignatura] = listNotas

# Visualización de datos. Se visualizan los valores de dicNot
print("Notas del alumno:")
for asignatura, notas in dicNot.items():
    print(f"{asignatura}: {notas}")

# Generar medias por asignaturas. Se calcula la media de las asginaturas
# Tambien preparo los valores para luego calcular la media final
suma_notasFinal=0
num_notasFinal=0
print("Medias por asignaturas:")
for asignatura, notas in dicNot.items():
    suma_notas = sum(notas)
    num_notas = len(notas)
    nota_media = suma_notas / num_notas
    #Valores que nos sirven para la media final
    suma_notasFinal+=suma_notas
    num_notasFinal+=num_notas
    print(f"{asignatura}: {nota_media}")
# Generar la nota media final del alumno. Se calcula y se escribe la nota final del alumno por pantalla
#print(num_notasFinal)
#print(suma_notasFinal)
print("********************************")
nota_media_final = suma_notasFinal / num_notasFinal
print(f"Nota media final del alumno: {nota_media_final}")
