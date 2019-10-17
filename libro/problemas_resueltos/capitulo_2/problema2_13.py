mat = int(input("Matrícula: "))
carr = str(input("Carrera: "))
sem = str(input("Semestre: "))
prom = float(input("Promedio: "))

if carr == "Economía":
	if sem > 5 and prom > 8.7:
		print(mat)
		print(carr)
		print("Aceptado")
elif carr == "Computación":
        if sem > 5 and prom > 8.4:
       		print(mat)
                print(carr)
                print("Aceptado")
elif carr == "Contabilidad":
        if sem > 4 and prom > 8.4:
                print(mat)
		print(carr)
		print("Aceptado")
