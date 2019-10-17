print("Ingrese 3 números reales que desee: ")
A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

if A > B:
	if A > C:
		print("A (%.1f) es el Mayor" %(A))
	elif A == C:
		print("A (%.1f) y C (%.1f) son los Mayores" %(A, C))
	else:
		print("C (%.1f) es el Mayor" %(C))
elif A == B:
	if A > C:
		print("A (%.1f) y B (%.1f) son los Mayores" %(A, B))
	elif A == C:
		print("A (%.1f), B (%.1f)" "y C (%.1f) son Iguales" %(A, B, C))
	else:
		pritn("C (%.1f) es el Mayor" %(C))
elif B > C:
	print("B (%.1f) es el Mayor" %(B)) 
elif B == C:
	print("B (%.1f) y C  (%.1f) son los Mayores" %(B, C))
else:
	print("C (%.1f) es el Mayor" %(C))

