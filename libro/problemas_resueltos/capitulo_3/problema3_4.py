# El programa, teniendo en cuenta ciertos criterios, calcula el aumento de sueldo
# para un grupo de trabajadores. Imprime el nuevo sueldo del trabajador y la nómina
# correspondiente

nom = 0

sue = float(input("Ingrese su sueldo: $"))

while sue != -1:
	if sue < 1001:
		nsue = sue * 1.15
	else:
		nsue = sue * 1.12
	nom += nsue
	print("Su nuevo sueldo será de %.2f" %(nsue))

	sue = float(input("Ingrese el siguiente sueldo: $"))

print("La nomina es de %.2f" %(nom))
