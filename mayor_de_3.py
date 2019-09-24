print("Ingrese 3 números cualesquiera:")
primero = int(input())
segundo = int(input())
tercero = int(input())

if primero < segundo:
	if segundo < tercero:
		print("El mayor es %d" %(tercero))
	else:
		print("El mayor es %d" %(segundo))
else:
	if primero < tercero:
		print("El mayor es %d" %(tercero))
	else:
		print("El mayor es %d" %(primero))

