num = int(input("Ingrese un número entero: "))

if num > 0:
	while (num != 1):
		print(num)
		
		if (-1 ** num) > 0:
			num = num / 2
		else:
			num = num * 3 + 1	
	print(num)

else:
	print("El numero ingresado tiene que ser un entero positivo")
