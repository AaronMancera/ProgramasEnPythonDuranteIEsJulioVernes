'''
Crear un programa que permita gestionar una agenda de teléfonos. 
Sabemos que de cada contacto se almacena dos datos, «nombre» y «teléfono» 
y que no se podrán crear contactos sin nombre ni teléfono.

La agenda permitirá realizar las siguientes operaciones: Añadir, buscar, modificar, 
eliminar, mostrar y vaciar.
Añadir: Permite agregar un nuevo contacto. Si ya existe un contacto con ese nombre 
se informará al usuario.
Buscar: Permite localizar un contacto por nombre.
Modificar: Modifica los datos de un contacto.
Eliminar: Elimina los datos de un contacto.
Mostrar: Muestra un listado de todos los contactos almacenados en la agenda.
Vaciar: Elimina todo el contenido de la agenda, previa confirmación del usuario.
'''
def annadir(nombre,telefono):
    agendaMovil[nombre]=telefono
def buscar(nombre):
    if nombre in agendaMovil:
        str=nombre+": "+agendaMovil[nombre]
    else:
        str="Error"
    return str    
def modificar(nombre):
    if buscar(nombre) != "Error":
        nuevoNombre=input("Introduce el nuevo nombre: ")
        nuevoTelefono=input("Introduce el nuevo numero de teléfono: ")
        eliminar(nombre)
        annadir(nuevoNombre,nuevoTelefono)

def eliminar(nombre):
    agendaMovil.pop(nombre)

agendaMovil={}
fin=False
while fin==False:
    print("-----------------")
    print("| 1   Añadir    |")
    print("| 2   Buscar    |")
    print("| 3  Modificar  |")
    print("| 4  Eliminar   |")
    print("| 5  Mostrar    |")
    print("| 6   Vaciar    |")
    print("| 7   Salir     |")
    print("-----------------")
    opcion=int(input("Escribe a que menu quieres entrar: "))
    while opcion>7 or opcion<1:
        opcion=int(input("Escribe a que menu quieres entrar: "))
    if opcion==7:
        fin=True
    elif opcion==1:
        print("+++++++++++++++++")
        nombre=input("Nombre para añadir: ")
        telefono=input("Numero de telefono: ")
        annadir(nombre,telefono)
        #print(agendaMovil)
    elif opcion==2:
        print("$$$$$$$$$$$$$$$$$")
        nombre=input("Nombre para buscar: ")
        print(buscar(nombre))
    elif opcion==3:
        print("/////////////////")
        nombre=input("Nombre para modificar: ")
        modificar(nombre)
    elif opcion==4:
        print("-----------------")
        nombre=input("Nombre para eliminar: ")
        eliminar(nombre)
    elif opcion==5:
        print(agendaMovil)
    elif opcion==6:
        agendaMovil.clear()
