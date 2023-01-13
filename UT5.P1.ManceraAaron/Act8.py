'''
    Solicitar un numero y decir si es primo
'''
num=int(input("Introduce un numero: "))
cont=0
text=""
for i in range(1,num+1):
    if(num%i==0):
        cont = cont+1
    if cont==2:
        text="Es primo"
    else:
        text="No es primo"
print(text)