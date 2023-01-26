import csv
'''
Dado el fichero estaciones.csv crea un programa que trabaje con el fichero, 
extraiga información, la muestra, … 

Todo el programa debe estar comentado. 

NINGÚN PROGRAMA ES “PARECIDO” AL DE OTRO COMPAÑERO/A

Se debe entregar zip con : 
Enunciado descriptivo como si fuera una tarea
Programa

'''
path="./UT5.P8.ManceraAaron/datos/estaciones.csv"

def mostrarDatosPaginados():
    cont=int(43)
    print("Cargando fichero en una página con 43 estaciones...")
    with open(path,encoding='utf-8') as file:
        lector = csv.reader(file)
        next(lector)
        for line in lector:
            print(line)
            cont-=1
            if cont==0:
                seguir=input("¿Quieres continuar a la siguiente página? (S/N): ")
                if seguir.lower() == "s":
                    print("---------------------------------------------------------------")
                    print()
                    cont=43
                elif seguir.lower() == "n":
                    break
    print()

def mostarOrdenados():
    cont=int(43)
    print("Cargando fichero en una página con 43 ordenado...")
    with open(path, encoding='utf-8') as file:
        lector = csv.DictReader(file)
        registros=[]
        for registro in lector:
            #name,slots,empty_slots,free_bikes,latitude,longitude
            name = registro['name']
            slots = registro['slots']
            empty_slots = registro['empty_slots']
            free_bikes = registro['free_bikes']
            latitude = registro['latitude']
            longitude = registro['longitude']
            tupla=(name,slots,empty_slots,free_bikes,latitude,longitude)
            registros.append(tupla)
    sort_registros=sorted(registros, key=lambda item: item[1], reverse=True)
    for r in sort_registros:
        print(f"{r[0]} : {r[1]}")
        cont-=1
        if cont==0:
            seguir=input("¿Quieres continuar a la siguiente página? (S/N): ")
            if seguir.lower() == "s":
                print("---------------------------------------------------------------")
                print()
                cont=43
            elif seguir.lower() == "n":
                break
    print()

def mostrarTodasConBiciletasLibres():
    cont=int(43)
    print("Cargando fichero en una página con 43 estaciones...")
    with open(path,encoding='utf-8') as file:
        lector = csv.reader(file)
        next(lector)
        for line in lector:
            if(int(line[3])>0):
                print(line[0])
                cont-=1
                if cont==0:
                    seguir=input("¿Quieres continuar a la siguiente página? (S/N): ")
                    if seguir.lower() == "s":
                        print("---------------------------------------------------------------")
                        print()
                        cont=43
                    elif seguir.lower() == "n":
                        break
    print()

def mostrarTodasConEspaciosLibres():
    cont=int(43)
    print("Cargando fichero en una página con 43 estaciones...")
    with open(path,encoding='utf-8') as file:
        lector = csv.reader(file)
        next(lector)
        for line in lector:
            if(int(line[2])>0):
                print(line[0])
                cont-=1
                if cont==0:
                    seguir=input("¿Quieres continuar a la siguiente página? (S/N): ")
                    if seguir.lower() == "s":
                        print("---------------------------------------------------------------")
                        print()
                        cont=43
                    elif seguir.lower() == "n":
                        break
    print()

def buscarEstacion():
    encontrado=False
    resultado=[]
    buscar=str(input("Escribe el nombre de la estacion para buscar: "))
    print("Cargando fichero y buscando...")
    with open(path,encoding='utf-8') as file:
        lector = csv.reader(file)
        next(lector)
        for linea in lector:
            if buscar.casefold() in linea[0].casefold():
                resultado=linea
                encontrado=True
    if encontrado==True:
        print(resultado)
    else:
        print("Nombre de la estación no encontrado...")

opcion=int(0)
while opcion!=6:
    print("-------- Bienvenido al programa GESTION DE ESTACIONES --------")
    print("|   1. Mostrar los datos paginado                            |")
    print("|   2. Mostar ordenado por espacios                          |")
    print("|   3. Mostrar todas las estaciones con bicicletas           |")
    print("|   4. Mostrar todas las estaciones espacio para bicicletas  |")
    print("|   5. Busqueda de estaciones por nombre                     |")
    print("|   6. Salir                                                 |")
    print("--------------------------------------------------------------")
    opcion=int(input("Introduce que opción quieres realizar: "))
    if opcion==1:
        print()
        print("Cargando opción...")
        mostrarDatosPaginados()
    elif opcion==2:
        print()
        print("Cargando opción...")
        mostarOrdenados()
    elif opcion==3:
        print()
        print("Cargando opción...")
        mostrarTodasConBiciletasLibres()
    elif opcion==4:
        print()
        print("Cargando opción...")
        mostrarTodasConEspaciosLibres()
    elif opcion==5:
        print()
        print("Cargando opción...")
        buscarEstacion()
    elif opcion==6:
        print("Adios")
