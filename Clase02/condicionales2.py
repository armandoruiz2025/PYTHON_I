"""
Crea un programa que solicite el monto 
total de una compra y aplique un descuento 
según el valor de la compra:

-Si la compra es menor a S/ 100 → 
no hay descuento.
-Si la compra está entre S/ 100 and S/ 299 → 
descuento del 5%.
-Si la compra está entre S/ 300 y S/ 499 → 
descuento del 10%.
-Si la compra es de S/ 500 a más → 
descuento del 15%.

El programa debe mostrar:
-El monto de la compra.
-El descuento.
-El monto descontado.
-El total que debe pagar.

💡 Pista: necesitarás if, elif, else y 
operaciones aritméticas.
"""

compra = float(input("Ingrese el monto de compra: "))
if compra<100:
    desc=0
elif compra<300: 
    desc= 5
elif compra<500:
    desc= 10
else:
    desc = 15
totdesc = desc/100
mondesc=compra-totdesc
total=compra-mondesc
print(f"El monto de la compra es {round(compra,2)} soles.")
print(f"El monto descontado es {round(mondesc,2)} soles.")
print(f"El monto total de es {round(total,2)} soles.")
