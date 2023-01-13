'''
Un anno es bisiesto si cumple los siguientes criterios:
Es divisible entre 4.
Si termina en 00, se comprueba si es divisible entre 400 
(2000 y 2400 sí son bisiestos. 2100, 2200 y 2300 no lo son).

Escribe una función que reciba un año y devuelva 1 si es bisiesto, 0 en caso contrario. La función no debe leer nada de la entrada estándar ni mandar ningún dato por la salida estándar.
La función debe definirse con este estilo:

def esBisiesto(anyo):

'''
def esBisiesto(anno):
    if anno % 4 != 0: #no divisible entre 4
        print("No es bisiesto")
    elif anno % 4 == 0 and anno % 100 != 0: #divisible entre 4 y no entre 100 o 400
        print("Es bisiesto")
    elif anno % 4 == 0 and anno % 100 == 0 and anno % 400 != 0: #divisible entre 4 y 10 y no entre 400
        print("No es bisiesto")
    elif anno % 4 == 0 and anno % 100 == 0 and anno % 400 == 0: #divisible entre 4, 100 y 400
        print("Es bisiesto")

anno=input("Escribe el año: ")
esBisiesto(float(anno))