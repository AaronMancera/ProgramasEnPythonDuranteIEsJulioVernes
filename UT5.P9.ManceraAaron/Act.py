import torch
'''
pip3 install torchvision para instalara la libreria

Esta libreria trabaja con tensores, que en terminos matematicos son matrices, por lo tanto se 
puede aplicar las operaciones matematicas como suma de matrices, producto de matrices, el producto a escalar

En este ejemplo se va a realizar una calculdara funcional de 2 tensores/matrices

'''


def asignarMatrices():
    print("Selecciona el tamaño NxM:")
    n=0
    while n<=1:
        n=int(input("m: "))
    m=0
    while m<=1:
        m=int(input("n: "))
    print("Asignando la matriz 1:")
    numeros11=[]
    for i in range(0,n):
        num=int(input("numero N: "))
        numeros11.append(num)
    numeros12=[]
    for i in range(0,m):
        num=int(input("numero M: "))
        numeros12.append(num)
    lista=[numeros11,numeros12]
    a=torch.tensor([lista])
    print("Asignando la matriz 2")
    numeros21=[]
    for i in range(0,n):
        num=int(input("numero N: "))
        numeros21.append(num)
    numeros22=[]
    for i in range(0,m):
        num=int(input("numero M: "))
        numeros22.append(num)
    lista=[numeros21,numeros22]
    b=torch.tensor(lista)
    return [a,b]

def sumaTensores(a,b):
    return a+b

def producto(a,b):
    d = torch.matmul(a, b.transpose(1, 0))
    return d

def productoEscalar(a,b):
    e = torch.dot(a.view(-1), b.view(-1))
    return e

def multiplicacion(a,b):
    f = a * b
    return f

#Calculadora de matrices
a=torch.empty
b=torch.empty
parametrosAsignados=False
opciones=0
while opciones!=6:
    print("-----Calculadora de dos Tensores-----")
    print("| 1. Asignar dos matrices           |")
    print("| 2. Sumar dos matrices             |")
    print("| 3. Producto de dos matrices       |")
    print("| 4. Producto a escalar             |")
    print("| 5. Multiplicar                    |")
    print("| 6. Salir                          |")
    print("-------------------------------------")
    opciones=int(input("Opción: "))
    if opciones==1:
        parametros=asignarMatrices()
        a=parametros[0]
        b=parametros[1]
        print(a)
        print(b)
        parametrosAsignados=True

    elif opciones==2 and parametrosAsignados==True:
        print(sumaTensores(a,b))
    elif opciones==3 and parametrosAsignados==True:
        print(producto(a,b))
    elif opciones==4 and parametrosAsignados==True:
        print(productoEscalar(a,b))
    elif opciones==5 and parametrosAsignados==True:
        print(multiplicacion(a,b))
    elif opciones==6 and parametrosAsignados==True:
        print("Saliendo...")
    else:
        print("Error: Numero de opcion incorrecto o sin asignar los tensores")