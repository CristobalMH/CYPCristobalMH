cuecer=0
n= int(input("Dame un numero entero positivo :"))

for i in range(1,n,1):
    num=int(input("Ingresa un entero :"))
    if num == 0:
        cuecer += 1


print("El numero de 0's capturaos fue: %.0f" %(cuecer))
