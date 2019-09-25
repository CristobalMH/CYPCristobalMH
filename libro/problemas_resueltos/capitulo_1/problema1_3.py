NOM = raw_input('Nombre del Dinosaurio: ')

PES = float(input("Ingrese el Peso del Dinosaurio en Toneladas: "))
LON = float(input("Ingrese la Longitud del Dinosaurio en Pies: "))

PESKIL = PES *1000
LONMET = LON * 0.3047

print("El Dinosaurio %s tiene un peso de %.0f kilogramos y una longitud de %.2f metros" %(NOM, PESKIL, LONMET))
