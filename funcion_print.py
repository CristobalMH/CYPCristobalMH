#print tiene 4 formas de uso
"""
1.- Comas
2.- Signo '+'
3.- Funcion format()
4.- Variante de format()
"""
#Comas, concatenar agregando
#un espacio y haciendo casting de tipo
edad = 10
nombre = "Juan"
estatura = 1.67
print(edad, estatura, nombre)

#Signo '+', hace lo mismo que con comas
#pero no realiza el casting automático
#no agrega espacio
print( str(edad) + str(estatura) + nombre )

#Función format()
print("Nombre: {1} Edad: {0} ".format(nombre, edad, estatura))

#Variante de format() simplificada
print(f"Nombre: \"{nombre}\" \nEdad:\t{edad} ")

#print y el argumento end
print("Solo hay 10 tipos de personas, las que saben binario y las que no",end="---")
print("otra linea")
