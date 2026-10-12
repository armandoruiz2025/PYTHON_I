productos = "CAFE","PAN","CAFE","GALLETA","GASEOSA"
#print(type(productos)) #Averiguar que tipo d datos es la variable

"""
COMPROBAR SI UN PRODUCTO EXISTE
"""
# if "PAN" in productos:
#     print("El Producto esta disponible")
# else:
#     print("El Producto NO esta disponible")

"""
CONTAR LAS APARACIONES DE UN VALOR
print(f"Veces que aparecio la palabra cafe {productos.count("CAFE")}")
"""


"""
OBTENER LA POSICION DE LA PRIMERA CONCIDENCIA
print(f"POSICION DE PAN {productos.index("CAFE")}")
"""

"""
DESEMPAQUETAR 
SIGNIFICA ASIGNAR LOS ELEMENTOS DE UNA TUPLA A VARIABLES
INDIVIDUALES22
"""

pedido =("CAFE",2,5.50)
producto,cantidad,precio = pedido
total = precio * cantidad
print(f"Precio unitario: S/.{precio:.2f} ")
print(f"Total: S/.{total:.2f} ")
