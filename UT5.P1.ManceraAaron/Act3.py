'''
    Actividad que suma 7 numeros y los multiplica
'''
suma=0
multi=1
max=7
i=0
for i in range(max):
    print("Numero ",i)
    numero=int(input())
    suma+=numero
    multi=numero*multi
print("La suma es: ",suma)
print("La multiplicacion es: ",multi)