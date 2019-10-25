med = 0
chi = 0
gra = 0

n = int(input("Ingrese un número entero: "))
i = 1

while i < n:
	v = float(input("Ingrese otro número entero: "))
	
	if v <= 200:
		chi += 1
	elif v <= 400:
		med += 1
	else:
		gra += 1
	i += 1

print("El número de ventas menores es %d" %(chi))
print("El número de ventas medias es %d" %(med))
print("El número de ventas mayores es %d" %(gra))

