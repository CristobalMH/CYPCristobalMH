sue = float(input("Ingrese su Sueldo :$ "))
cate = int(input("Ingrese su Categoría : "))
he = int(input("Horas Extras: "))

phe = 0

if cate == 1:
	phe = 30
elif cate == 2:
	phe = 38
elif cate == 3:
	phe = 50
elif cate == 4:
	phe = 70
else:
	phe = 0

nsue = 0

if he > 30:
	nsue = sue + 30 * phe
else:
	nsue = sue + he * phe

print("Su nuevo sueldo es de $%d" %(nsue))
