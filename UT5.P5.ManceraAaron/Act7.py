import random
'''
Escribir una función que aplique un descuento a un producto (recibirá como parámetros 
el descuento a aplicar y el precio del artículo) y otra que aplique el IVA 
(recibirá como parámetros el IVA a aplicar y el precio del artículo) . 
Escribir una tercera función calcularImporteFinal que reciba un diccionario con los precios y 
porcentajes de una  serie de artículos y una de las funciones anteriores. 
CalcularImporteFinal utilizará la función pasada como segundo argumento  
para aplicar los descuentos o el IVA a los productos y devolver la suma total de los precios 
finales de los artículos.
Utilizar el paso de parámetros en las 3 funciones.
'''
#Esta funcion define el descuento del producto y tambien lo aplica al precio del diccionario
def definirDescuento(nombre,descuento):
    for i in productos:
        producto={}
        if nombre==productos[i]["Nombre"]:
            producto=productos[i]
            producto["Descuento"]=descuento
            producto["Precio"]=float(producto["Precio"] - (float(producto["Precio"])*float(descuento)/100) )
        
#Esta funcion define el iva del producto y tambien lo aplica al precio del diccionario
def definirIVA(nombre,iva):
    for i in productos:
        producto={}
        if nombre==productos[i]["Nombre"]:
            producto=productos[i]
            producto["IVA"]=iva
            producto["Precio"]=(float(producto["Precio"])*float(iva)/100) + float(producto["Precio"])


productos={}
nombre=("Patatas","Pizza","Bocadillo de atun","Ensalada")
#Creacion
for i in range (len(nombre)):
    producto={}
    producto["Nombre"]=nombre[i]
    producto["Precio"]=random.randint(1,100)
    productos[i]=producto
#print(productos)

print("Ahora vas a definir los descuentos de los productos")
for i in productos:
    nombre=productos[i]["Nombre"]
    print("Productos: "+nombre)
    descuento=input("Escriba el descuento (sin %): ")
    definirDescuento(nombre,descuento)
#print(productos)
print("Ahora vas a definir el IVA de los productos")
for i in productos:
    nombre=productos[i]["Nombre"]
    print("Productos: "+nombre)
    iva=input("Escriba el iva (sin %): ")
    definirIVA(nombre,iva)
#print(productos)
