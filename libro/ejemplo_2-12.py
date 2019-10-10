A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

if A > B:
	if A > C:
		if B > C:
			print("%d, %d, %d" %(A, B, C))
		else:
			print("%d, %d, %d" %(A, C, B))
	else:	
		print("%d, %d, %d" %(C, A, B))
else:
	if B > C:
		if A > C:
			print("%d, %d, %d" %(B, A, C))
		else:
			print("%d, %d, %d" %(B, C, A))
	else:
		print("%d, %d, %d" %(C, B, A))

print("Fin del Programa")
