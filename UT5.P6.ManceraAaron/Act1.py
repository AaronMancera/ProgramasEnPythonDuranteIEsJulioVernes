'''
Se pide crear un programa para EMVISESA (Empresa municipal para la vivienda en Sevilla) 
que se encargue de manejar y filtrar la lista de inmuebles existente. 

Sabemos que, por ahora, la lista de pisos que maneja es la siguiente:
[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
Se pide crear las siguientes funciones:
Función que reciba la lista de inmuebles y la devuelva incorporando un nuevo par 
a cada diccionario con el precio del inmueble. El precio de un inmueble se calcula con 
las siguiente fórmula en función de la zona:
Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000)
Zona B: precio = (metros * 1200 + habitaciones * 5500 + garaje * 16000)

Función que permite hacer búsqueda de inmuebles en función de un presupuesto dado. 
La función recibirá como entrada la lista de inmuebles y un precio,
y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado.
'''
#Se pasa por parametro un inmueble y se calcula su precio dependiendo de la zona
def calcular_precio_inmueble(inmueble):
    print(inmueble)
    if inmueble['zona'] == 'A':
        inmueble['precio'] = inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + inmueble['garaje'] * 15000
    elif inmueble['zona'] == 'B':
            inmueble['precio'] = inmueble['metros'] * 1200 + inmueble['habitaciones'] * 5500 + inmueble['garaje'] * 16000
    return inmueble
#Se busca dentro del diccionario de inmueble cuales son los que te puedes permitir
def buscar_inmuebles(dicDeInmueble,presupuesto):
    resultado = []
    for i in range(len(dicDeInmueble)):
        if dicDeInmueble[i]['precio'] <= presupuesto:
            resultado.append(dicDeInmueble[i])
    return resultado

listaDePisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
                {'año': 2012, 'metros': 60, 'habitaciones': 2,
                    'garaje': True, 'zona': 'B'},
                {'año': 1980, 'metros': 120, 'habitaciones': 4,
                    'garaje': False, 'zona': 'A'},
                {'año': 2005, 'metros': 75, 'habitaciones': 3,
                    'garaje': True, 'zona': 'B'},
                {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
dicDeInmueble ={}
for i in range(len(listaDePisos)):
    dicDeInmueble[i]=listaDePisos[i]
print(dicDeInmueble)
print("/////////////////////////////")
print("Calculo de los inmuebles")
for i in range(len(dicDeInmueble)):
    #print(dicDeInmueble[i])
    calcular_precio_inmueble(dicDeInmueble[i])
print(dicDeInmueble)
print("/////////////////////////")
print("Lista de productos que puedes adquirir con un presupuesto de 130000")
presupuesto=130000
resultado=buscar_inmuebles(dicDeInmueble,presupuesto)
print(resultado)