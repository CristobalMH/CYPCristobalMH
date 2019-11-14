archivo = open("archivo.txt","rt")

numeros1 = archivo.read()
print(numeros1)
print(numeros1.split('\n'))
print(numeros1.split())
lista_num = []
for linea in numeros1.split('\n'):
    for numero in linea.split(','):
        lista_num.append(str(numero))
print("%s" %(lista_num))
lista_num.sort()
print("Lista ordenada:{lista_num}"'\n')
print("El mayor es: %s y el menor es: %s" %(lista_num[-1], lista_num[0]))
archivo.close()

lista_num = []
for linea in numeros1.split():
    for numero in linea.split(','):
        lista_num.append(str(numero))
print("%s" %(lista_num))
lista_num.sort()
print("Lista ordenada: %s" %(lista_num))
print("El mayor es: %s y el menor es: %s" %(lista_num[-1], lista_num[0]))
archivo.close()

archivo=open("archivo.txt","rt")
numero2 = archivo.readlines()
print(numero2)
archivo.close()

archivo=open("archivo.txt","rt")
numero2 = archivo.readline()
print(numero2)
archivo.close()
