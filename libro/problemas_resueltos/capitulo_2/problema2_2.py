print("Ingrese valores enteros para las variables P y Q") 

P = int(input())
Q = int(input())

EXP = P**3 + Q**4 -2 * P**2

if EXP < 680:
	print("Los valores de P y Q son satisfactorias")
	print("%d, %d" %(P, Q))
	print("%d" %(EXP))
else: 
	print("Suerte para la proxima")

