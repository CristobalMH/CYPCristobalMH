print("Ingrese valores reales para las variables A, B y C")

A = float(input())
B = float(input())
C = float(input())

DIS = B**2-4*A*C

if DIS >= 0:
	X1 = ((-B)+DIS**0.5/2*A)
	X2 = ((-B)-DIS**0.5/2*A)
	
	print("Las raices utilizando las Variables A, B y C son reales")
	print("DIS = %d, X1 = %.2f y X2 = %.2f" %(DIS, X1, X2))
else:
	print("Las raices utilizando las Variables A, B y C no son reales")

print("Fin del programa")
