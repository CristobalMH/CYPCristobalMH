#Area de un Cilindro

import math

PI = math.pi

RADIO = float(input("Radio: "))
ALTU = float(input("Altura: "))

VOL = PI * (RADIO **2) * ALTU
ARE = 2 * PI * RADIO * ALTU

print("El cilindro tiene un Volumen de %.2f y un Área de %.2f" %(VOL,ARE))
