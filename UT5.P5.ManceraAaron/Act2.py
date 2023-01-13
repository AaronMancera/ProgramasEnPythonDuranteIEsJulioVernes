'''
Definir una función de nombre descuento que reciba como parámetro un valor y un porcentaje 
y devuelva el resultado de aplicar el descuento correspondiente 
al porcentaje sobre el valor indicado.

Ejecuta después las siguientes líneas: 
precio = 200
print("Precio con 10% de descuento:", descuento(precio, 10))
'''
def descuento(valor,porcentaje):
    return str(float(valor)*float(porcentaje)/100)

valor=input("Escribe el precio del producto: ")
porcentaje=input("El descuento del producto: ")
print(f"El precio con {porcentaje}% de descuento: "+descuento(valor,porcentaje))