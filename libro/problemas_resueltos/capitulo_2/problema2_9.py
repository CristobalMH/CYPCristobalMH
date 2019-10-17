prebas = float(input(" Ingrese el precio del producto: "))
imp = 0
pretot = 0

if prebas > 500:
	imp = 20 * .30 + (prebas - 40) * .50
elif prebas > 40:
	imp = 20 * .30 + (prebas - 40) * .40
elif prebas > 20:
	imp = (prebas - 20) * .30
else:
	imp == 0

pretot = prebas + imp

#print(imp)
print("El precio básico del producto es $%.2f" %(prebas))
print("El precio del producto más el impuesto es de $%.2f" %(pretot))
