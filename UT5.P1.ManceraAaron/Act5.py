'''
    Actividad que tienes que poner 3 numeros y decir si alguno de los tres es mayor de 10
'''
resultado=""
i=0
for i in range(0,3):
    num = int(input("Introduce un numero: "))
    if(num>10):
        resultado="Alguno de los 3 números es mayor que 10"
    elif(resultado==""):
        resultado="Ninguno de los 3 números es mayor que 10"
print(resultado)