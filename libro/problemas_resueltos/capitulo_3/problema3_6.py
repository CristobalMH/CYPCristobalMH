may = -100000
men = 100000

n = int(input("Ingrese un Número entero: "))
i = 1

while i < n:
	num = int(input("Ingrese otro número entero: "))
	
	if num > may:
		may = num
	
	if num < men:
		men = num

	i += 1
print("El valor máximo es de %d" %(may))
print("El valor mínimo es de %d" %(men))
