'''
Crear un programa en Python que nos permita guardar los nombres de los alumnos de una clase 
y sus notas. 
Se solicitará al usuario el número de alumnos , luego se pedirá su nombre y sus notas 
(cada alumno puede tener distinto número de notas y sabemos que finaliza la lectura de ellas cuando el usuario introduzca un número negativo.). 
Tras la carga de datos se calculará la media de cada alumno y se visualizará la lista de todos 
los alumnos con sus medias.
Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.
'''
# Diccionario alumnos
alumnos = {}
# Solicitar al usuario el número de alumnos
num_alumnos = int(input("Introduce el número de alumnos: "))
# Recorrer un bucle insertando tantos alumnos como num_alumnos haya
for i in range(num_alumnos):
    # Solicitar nombre del alumno
    nombre = input("Introduce el nombre del alumno: ")
    # Comprueba si el alumno ya existe en la lista
    while nombre in alumnos:
        print("Error: el alumno ya existe en la lista, vuelva a intentarlo.")  
        nombre = input("Introduce el nombre del alumno: ")
    # Crear una lista vacía para almacenar las notas del alumno
    notas = []
    # Solicitar notas del alumno
    nota = float(input("Introduce una nota del alumno (introduce un número negativo para finalizar): "))
    while nota >= 0:
        notas.append(nota)
        nota = float(input("Introduce una nota del alumno (introduce un número negativo para finalizar): "))
    # Calcular media del alumno
    media = sum(notas) / len(notas)
    # Agregar el alumno, con su media, al diccionario
    alumnos[nombre] = media

# Imprimir la lista de alumnos con sus medias
for alumno, media in alumnos.items():
    print(f"{alumno}: {media}")