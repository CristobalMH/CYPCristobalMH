#Pide datos de entrada para la base y la altura y obtiene la superficie y el perimetro

BASE = float(input("BASE ="))
ALTURA = float(input("ALTURA ="))

SUP = BASE * ALTURA
PER = 2 * (BASE + ALTURA)

print("La superficie de la figura es de", SUP, "unidades cuadradas")
print("El perimetro de la figura es de", PER, "unidades")
