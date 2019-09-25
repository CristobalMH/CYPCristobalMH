#Ingrese las coordenadas de dos puntos para obtener la distancia entre ambos

X1 = float(input("X1 = "))
Y1 = float(input("Y1 = "))

X2 = float(input("X2 = "))
Y2 = float(input("Y2 = "))

DIS = ((X1-X2) ** 2 + (Y1-Y2) ** 2) ** 0.5

print("La distancia entre los puntos A(%.2f, %.2f) y B(%.2f, %.2f) es %.2f" %(X1, Y1, X2, Y2, DIS))
