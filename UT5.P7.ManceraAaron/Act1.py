'''
Escribe un programa que escriba los 100 primeros numeros naturales en el archivo numeros.txt
'''
with open("./UT5.P7.ManceraAaron/ficheros/numeros.txt", mode='w', encoding='utf-8') as f:
    print("Escribiendo en el fichero...")
    for i in range(1,100):
        f.write(str(i)+' ')
