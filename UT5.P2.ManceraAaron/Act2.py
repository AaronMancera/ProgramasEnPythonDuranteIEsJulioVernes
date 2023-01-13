'''
Escribir un programa que a través de un menú permita al usuario 
sumar, restar, multiplicar o dividir dos operandos. 
El menú tendrá la opción 5 de salir.
'''
opcion=0
num1=0
num2=0
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multi(a,b):
    return a*b
def divi(a,b):
    return a/b
try:
    while(opcion!=5):
        print("********************")
        print("* 1. Sumar         *")
        print("* 2. Restar        *")
        print("* 3. Multiplicar   *")
        print("* 4. Dividir       *")
        print("* 5. Salir         *")
        print("********************")
        opcion=int(input("Opcion: "))
        if(opcion<5 and opcion>0):
            num1=float(input("Numero 1: "))
            num2=float(input("Numero 2: "))
            if(opcion==1):
                print(f"Resultado: {suma(num1,num2)}")
            elif(opcion==2):
                print(f"Resultado: {resta(num1,num2)}")
            elif(opcion==3):
                print(f"Resultado: {multi(num1,num2)}")
            elif(opcion==4):
                print(f"Resultado: {divi(num1,num2)}")
except ValueError:
    print("No se puede llevar a cabo la operación")