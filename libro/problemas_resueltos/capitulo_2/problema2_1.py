N = int(input("Ingrese el número de sonidos emitidos por un grillo por minuto: "))
T = 0

if N > 0:
	T = N / 4 + 40
	print("La Temperatura es de %.2f°F" %(T))
else:
	print("No hay grillo")

