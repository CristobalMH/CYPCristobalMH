SUE = float(input("Ingrese su saldo actual: "))

if SUE < 1000:
	AUM = SUE * 0.15
	NSUE = SUE + AUM
	print("Tiene un aumento de $ %.2f" %(AUM))
	print("Su nuevo sueldo es de $ %.2f" %(NSUE))
else:
print("Su saldo sigue siendo de $ %.2f" %(SUE))
