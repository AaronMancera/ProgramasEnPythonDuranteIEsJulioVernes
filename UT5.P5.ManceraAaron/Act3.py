'''
El factorial de n se define en principio como el producto de todos los números enteros 
positivos desde 1 (es decir, los números naturales) hasta n. En el caso de 0, el resultado es 1.

Escribe una función que reciba un entero entre 0 y 10 y calcule su factorial.
La función debe definirse con este estilo: def factorial(num):

n! = n * (n-1) * (n-2) * (n-3) * …* 1
Ejemplo cálculo factorial:
6! = 6*5*4*3*2*1 = 720
'''
def factorial(num):
    resultado=1
    cadena=num+"!="
    for i in range(int(num),1,-1):
        resultado=float(resultado*i)
        cadena=cadena+str(i)+"*"
    cadena=cadena+"1 = "+str(resultado)
    print(cadena)
        

num=input("Escribe el numero que le vas a hacer factorial: ")
factorial(num)