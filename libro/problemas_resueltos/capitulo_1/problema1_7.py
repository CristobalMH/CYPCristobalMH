#Area_Triangulo


print("Ingrese las medidas para los lados de un triangulo: ")
L1 = float(input("Primer Lado = "))
L2 = float(input("Segundo Lado = "))
L3 = float(input("Tercer Lado = "))

S = (L1 + L2 + L3)/2
AREA = (S * (S-L1) * (S-L2) * (S-L3)) ** 0.5

print("Calculo Auxiliar = %.2f" %(S))
print("Area = %.2f" %(AREA))
