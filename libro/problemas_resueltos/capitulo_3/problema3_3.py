# El programa calcula el resultado de una determinada serie

serie = 0

n = int(input("Ingrese un número entero: "))

band = 'T'
i = 1

while i < n:
	if band == 'T':
		serie += 1/n
		band = 'F'
	else:
		serie += 1/n
		band = 'T'
	i += 1

print(serie)
