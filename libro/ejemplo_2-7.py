NUM = int(input("Ingrese un número entero positivo: "))
V = int(input("Ingrese otro número entero positivo: "))
VAL = 0

if NUM == 1:
	VAL = 100 * V
elif NUM == 2:
	VAL = 100 ** V
elif NUM == 3:
	VAL = 100 / V
else:
	VAL = 0

print(VAL)
print("Fin del Programa") 
