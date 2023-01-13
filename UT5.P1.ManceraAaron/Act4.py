'''
    Actividad que suma los numeros que quieras y los multiplica
'''
numero=-1
suma=0
multi=1
i=0
print("Cantidad de numeros")
max=int(input())
for i in range(max):
    while(numero<0):
        print("Numero ",i)
        numero=int(input())
    suma+=numero
    multi=numero*multi
    numero=-1
print("La suma es: ",suma)
print("La multiplicacion es: ",multi)