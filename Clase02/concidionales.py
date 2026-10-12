
#Devuelve que tipo de datos es la variable
#print(type(edad))
"""
La indentación es el espacio que se deja 
al inicio de una línea de código. 
En Python sirve para indicar qué 
instrucciones pertenecen a un bloque de 
código.
"""
#EJER01.-Comprobar si es mayor de edad
#edad = int(input("Ingrese la edad:"))#P1
#if edad>=18:#P2
#    print("Es Mayor de edad") #P3 
#else:
#    print("Es Menor de edad")    
#EJER02.-Aplicar un descuento del 50 a las ventas
# mayores a 1000
ventas = float(input("Ingrese las ventas:"))
if ventas>1000:
    desc=50
else:
    desc=0
total = ventas - desc            
print(f"El Total a pagar es {round(total,2)}")
"""
Crea un programa que solicite un número entero. 
Si el número es divisible entre 2, debe mostrar 
que es par. En caso contrario, debe mostrar que es impar.
"""
num = int(input("Ingresa un número: "))

if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")