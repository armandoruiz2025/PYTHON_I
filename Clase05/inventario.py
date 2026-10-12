"""
"""
productos  = ["Laptop","Mouse","Teclado","Monitor"]
precios  = [2500,50,120,110]
stock = [5,20,15,8]
print("=========Inventario================")
#Funcion len me indica la cantidad de items que tiene
#La Lista
for i in range(len(productos)):
    print(productos[i]," ",precios[i]," ",
          stock[i],"Und")

productos_sin_stock=[productos[i] for i in 
                     range(len(productos)) 
                     if stock[i] < 10]
print(productos_sin_stock)
"""
COMPRENSION DE LISTAS
- Obtener los productos que tiene stock menor a 10
"""

