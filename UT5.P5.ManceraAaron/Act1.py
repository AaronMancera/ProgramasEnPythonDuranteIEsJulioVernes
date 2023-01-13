'''
Escribe un programa con una función suma(n1,n2). 
Debe solicitar dos números y calcular su suma
'''
def suma(num1,num2):
    return float(num1)+float(num2)

num1=input("Escribe el primer numero: ")
num2=input("Escribe el segundo numero: ")
print(suma(num1,num2))