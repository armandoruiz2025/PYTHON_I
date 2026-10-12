"""
Costantes son variables que no van a 
cambiar su valor en el trasncurso del program
y se definen en mayusculas X convenciones 
"""
VALOR_IGV = 0.18
PI = 3.14
precio = input("Ingrese el precio del producto:")
can = input("Ingrese la cantidad del producto:")
#cast es convertir de un tipo a otro
subtotal = float(precio) * int(can)
#round sirve para redondear valores decimales
print(f"El Total a pagar es {round(subtotal,2)}")
