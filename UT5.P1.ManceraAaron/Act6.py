'''
    Nuevo sueldo. 
    Calcular si un empleado aumenta su sueldo. 
    Para ello solicitaremos dos valores enteros: sueldo y antigüedad. 
'''
    
sueldo=float(input("Sueldo en €: "))
antiguedad=int(input("Antigüedad en años: "))
if(sueldo<500 and antiguedad>10):
    sueldo=sueldo*3
elif(sueldo<500 and antiguedad<=10): 
    sueldo=sueldo*2
print("El sueldo resultante es:",sueldo, "con ",antiguedad," de antigüedad")