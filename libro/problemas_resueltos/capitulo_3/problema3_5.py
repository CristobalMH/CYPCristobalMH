sumotr = 0
sumpos = 0
cuepos = 0

n = int(input("Ingrese un número entero: "))
i = 1

while i < n:
	num = int(input("Ingrese otro número entero: "))
	
	if num > 0:
		sumpos += num
		cuepos += 1
	else:
		sumotr += num

	i += 1

progen = (sumpos + sumotr)/n
propos = (sumpos / cuepos)

print("Los números positivos son %d, el promedio de los números positivos es %.2f" %(cuepos, propos))
print("El promedio general es de %.2f" %(progen))
