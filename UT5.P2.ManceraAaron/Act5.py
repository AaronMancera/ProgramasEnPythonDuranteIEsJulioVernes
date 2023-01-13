'''
Escribir un programa en el que se pregunte 
al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece
la letra en la frase.
'''
print("Introduce una frase: ")
frase=input()
print("¿Qué palabra quieres buscar?")
palabra=input()
cont=frase.count(palabra)
print(f"La cantidad de veces que aparece {palabra} en la frase: {cont}")