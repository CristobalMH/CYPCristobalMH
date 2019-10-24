sumpar = 0
sumimp = 0
cuepar = 0

for i in range (1, 10, 1):
	num = int(input("Ingrese un número (1 - 270)"))
	if num != 0:
		if ((-1) ** num) > 0:
			sumpar += num
			cuepar += 1
		else:
			sumimp += num

propar = sumpar / cuepar

print("El promedio de los números pares es: %.2f y la suma de los números impares es %d" %(propar, sumimp))
