print("Introduzca 3 números enteros:")

A = int(input())
B = int(input())
C = int(input())

if A < B:
	if B < C:
		print("Los Números están en orden creciente")
	else:
		print("Los Números no están en orden creciente")
else:
	print("Los Números no están en orden creciente")
