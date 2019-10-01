MAT = int(input("Ingrese su numero de cuenta: "))

print("Ingrese sus 5 calificaciones para obtener el promedio")

CAL1 = float(input())
CAL2 = float(input())
CAL3 = float(input())
CAL4 = float(input())
CAL5 = float(input())

PRO = (CAL1 + CAL2 + CAL3 + CAL4 + CAL5)/5

if PRO >= 6:
	print("El alumno con la matricula %d APROBO ya que tiene un promedio de %.2f" %(MAT, PRO))
else:
	print("El alumno con la matricula %d REPROBO ya que tiene un promedio de %.2f" %(MAT, PRO))
