'''
    Actividad pone una base y exponente y lo hace en una función
'''
def funcion(a,b):
    calculo=float(a)**float(b)
    return calculo
print('Base:')
base=input()
print('Exponente:')
exponente=input()
calculo=funcion(base,exponente)
print(calculo)

