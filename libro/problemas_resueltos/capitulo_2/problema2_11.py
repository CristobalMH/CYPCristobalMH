print("Clave - Zona Geográfica")
print("12 - América del Norte")
print("15 - América Central")
print("18 - América del Sur")
print("19 - Europa")
print("23 - Asia")
print("25 - África")
print("29 - Oceanía")

clave = int(input("Ingrese la clave de la Zona desde donde está haciendo la llamada: "))

cost = 0

num = int(input("Ingrese los minutos de durción de la llamada: "))

if clave == 12:
	cost = num * 2
elif clave == 15:
	cost = num * 2.2
elif clave == 18:
	cost = num * 4.5
elif clave == 19:
	cost = num * 3.5
elif clave == 23 or clave == 25:
	cost = num * 6
elif clave == 29:
	cost = num * 5

print("El costo de la llamada ealizada es de $%.1f" %(cost)) 
