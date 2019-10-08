CATE = int(input("Ingrese la Categoría del Trabajador (1-4): "))
SUE = float(input("Ingrese el Sueldo del Trabajador: $"))
NSUE = 0

if CATE == 1:
	NSUE = SUE * 1.15
elif CATE == 2:
	NSUE = SUE * 1.10
elif CATE == 3:
	NSUE = SUE * 1.08
else:
	NSUE = SUE * 1.07

print("El Trabajador con la Categoría %d, tiene un Nuevo Sueldo de $%.2f" %(CATE, NSUE))
