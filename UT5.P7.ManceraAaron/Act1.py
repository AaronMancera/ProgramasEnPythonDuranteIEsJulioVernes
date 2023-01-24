'''
Escribe un programa que escriba los 100 primeros numeros naturales en el archivo numeros.txt
'''
with open("ficheros/numeros.txt", mode='w', encoding='utf-8') as f:
    for i in range(1,100):
        f.write(i+' ')