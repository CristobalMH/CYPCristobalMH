enf = int(input("Tipo de enfermedad del paciente (1-4): "))
edad = int(input("Edad del paciente: "))
dias = int(input("Dias de hospitalizacion:"))

costot = 0

if enf == 1 :
    costot = dias * 25
elif enf == 2 :
    costot = dias * 16
elif enf == 3 :
    costot = dias * 20
elif enf == 4 :
    costot = dias * 32

if edad >= 14 and edad <= 22 :
    costot *= 1.1

print("El costo total del paciente es de $%d" %(costot))
