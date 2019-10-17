compra = float(input("Ingrese el Monto de la Compra Realizada: "))

if compra < 500:
	print("Usted no tiene descuento, tiene que pagar $%d" %(compra)) 
elif compra <= 1000:
	desc_5 = compra - (compra*.05)
	print('Usted tiene que pagar %.2f tiene un descuento del 5' %(desc_5))
elif compra <= 7000:
	desc_11 = compra - (compra*0.11)
	print('Usted tiene que pagar %.2f tiene un descuento del 11' %(desc_11))
elif compra <= 15000:
        desc_18 = compra - (compra*0.18)
        print('Usted tiene que pagar %.2f tiene un descunto del 18' %(desc_18))
else:
        desc_25 = compra - (compra*0.25)
        print('Usted tiene que pagar %.2f tiene un descuento del 25' %(desc_25))
