import random
'''
    Vamos a crear una aplicación que tire miles de dados por segundo,
    la aplicación parara cuando todos los dados que le digamos estén en 6,
    por ejemplo si le digo que quiero que 5 dados coinciden
    en 6 hará tiradas hasta que 5 dados seguidos de 6.
    Para esto usaremos una lista!

    El script que vais a crear empezará preguntando cuántos dados queremos,
    después de esto se pondrá a hacer las tiradas, cuando se dé el caso de que
    ha salido el dado 6 el número de veces que le indicamos, parara,
    nos printeara la lista y el número de intentos que hemos hecho.

    RETO: En las tiradas, si más de la mitad de los dados están en seis 
    que nos printee la lista también!
'''

dados=[]
cont=0
contIguales=0
nDados=0
nDadosIguales=0
print("Cuantos dados con 6 quieres tener: ")
nDados=input()
print("Tirando dados...")
terminado=False
while terminado == False :
    num=random.randint(1,6)
    cont+=1
    dados.append(num)
    if num==6:
        nDadosIguales+=1
        if nDadosIguales==int(nDados):
            terminado=True
print(f"Numero de veces que te ha costado: {cont} ")
print(f"La lista de dados es {dados}")

