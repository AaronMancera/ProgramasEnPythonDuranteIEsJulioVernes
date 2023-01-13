'''
Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
    La temperatura media de cada día
    Los días con menos temperatura
    Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.
'''
locaclizaciones=[]
temperaturasMinimas=[]
temperaturasMaxima=[]
temperaturaMedia=[]

for i in range(1,6):
    print(f"Localizacion {i}:")
    locali=input()
    locaclizaciones.append(locali)
    print("Temperatura maxima del lugar:")
    tempe=int(input())
    temperaturasMaxima.append(tempe)
    tempeMin=tempe+1
    while tempe < tempeMin:
        print("Temperatura minima del lugar:")
        tempeMin=int(input())
        temperaturasMinimas.append(tempeMin)
tempM=100
menosTemp=0
for i in range(len(locaclizaciones)):
    media=0
    media+=temperaturasMinimas[i]
    media+=temperaturasMaxima[i]
    media/=len(temperaturasMinimas)
    temperaturaMedia.append
    if(temperaturasMinimas[i]<tempM):
        tempM=temperaturasMinimas[i]
        menosTemp=i
    print(f"Localizacion: {locaclizaciones[i]}")
    print(f"La media es: {temperaturasMinimas[i]}")

print(f"La de menos temperatura es: {locaclizaciones[menosTemp]}")

print("Introduce una temperatura maxima para buscar: ")
buscar=int(input())
maximaTemp=0
print("La temperatura maximas encontradas son: ")
for i in range(len(temperaturasMaxima)):
    if(temperaturasMaxima[i]==buscar):
        maximaTemp=temperaturasMaxima[i]
        maximaTemp=i
        print(f"{locaclizaciones[i]}    {temperaturasMaxima[i]}")
if(maximaTemp==0):
    print("Error, temperatura maxima no encontrada")