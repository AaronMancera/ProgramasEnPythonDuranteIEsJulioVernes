'''
    Solicitar una nota (float) y mostrar mensaje
'''
nota=float(input("Introduce la nota del alumno: "))
if(nota<3):
    print("Muy insuficiente")
elif(nota<5):
    print("Insuficiente")
elif(nota<6):
    print("Suficiente")
elif(nota<7):
    print("Bien")
elif(nota<9):
    print("Notable")
elif(nota<11):
    print("Sobresaliente")