'''
Crea un programa que permita introducir a un profesor las notas de sus estudiantes 
(máximo 10 estudiantes).
Una vez introducidos todos los datos, el programa mostrará una lista con los nombres 
de los estudiantes que han suspendido y otra con los que han aprobado. 
También calculará y mostrará la nota media de la clase
'''

#diccionario de profes
diccionarioProfesores={}

profesor=input("Introduce el nombre del profesor: ")
diccionarioProfesores["profesor"]=profesor
diccionarioEstudiantes={}
for i in range(1,11):
    diccionarioAlumno={}
    if i==10 :
        break
    alumno=input("Introduce el nombre de un alumno (max 10/acabar con 0): ")
    if alumno=="0":
        break
    nota=(input(f"Introduce la nota de {alumno}: "))
    diccionarioEstudiantes[i]=""
    diccionarioAlumno["nombre"]=alumno
    diccionarioAlumno["nota"]=nota
    diccionarioEstudiantes[i]=diccionarioAlumno
diccionarioProfesores["estudiantes"]=diccionarioEstudiantes
print(diccionarioProfesores)
#Tratamiento de suspensos, aprobados y la media
suspensos=[]
aprobados=[]
suma=0
print("-------------------")
for i in diccionarioProfesores["estudiantes"]:
    suma+=float(diccionarioProfesores["estudiantes"][i].get("nota"))
    if float(diccionarioProfesores["estudiantes"][i].get("nota")) < 5:
        suspensos.append(diccionarioProfesores["estudiantes"][i].get("nombre"))
    else:
        aprobados.append(diccionarioProfesores["estudiantes"][i].get("nombre"))
media=suma/len(diccionarioProfesores["estudiantes"])
print("Aprobados")
print(aprobados)
print("Suspensos")
print(suspensos)
print("Media")
print(media)