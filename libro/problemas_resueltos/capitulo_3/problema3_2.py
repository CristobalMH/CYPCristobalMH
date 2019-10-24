# El programa imprime y suma los términos de una serie

sumser = 0
band = 'T'
i = 2

while i <= 1800:
	sumser += 1
	print(i)
	
	if band == 'T':
		band = 'F'
		i += 3
	else:
		band = 'T'
		i += 2

print("La suma de la serie es: %d" %(sumser))
