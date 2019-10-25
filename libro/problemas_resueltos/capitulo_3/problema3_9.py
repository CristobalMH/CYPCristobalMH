serie = 0

n = int(input("Introduzca un número: "))
i = 1

while (i <= n):
	serie += i ** i
	i += 1

print("El acumulado de la serie es %.2f" %(serie))
