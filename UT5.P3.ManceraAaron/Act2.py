'''
    Se quiere realizar un programa que lea por teclado las 5 notas obtenidas 
    por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar 
    todas las notas,la nota media, la nota más alta que ha sacado y la menor.
'''
notas=[]
notaMedia=0
notaMasAlta=0
notaMasBaja=10
for i in range(0,5):
    print(f"Cual es la nota del alumno {i}: ")
    nota=-1
    while(nota<0 or nota>10):
        nota=int(input())
    notas.append(nota)
    notaMedia+=nota

print("Muestra de todos la nota de los alumnos:")
for i in notas:
    print(i)
    if(i>notaMasAlta):
        notaMasAlta=i
    if(i<notaMasBaja):
        notaMasBaja=i
print("La nota media es la siguiente: ")
print(notaMedia/5)
print("La nota mas alta es la siguiente: ")
print(f"El indice en las lista es: {notas.index(notaMasAlta)} y la nota es: {notaMasAlta}")
print("La nota mas baja es la siguiente: ")
print(f"El indice en las lista es: {notas.index(notaMasBaja)} y la nota es: {notaMasBaja}")
