"""
COMO USAR WHILE

- Se usa cuando repetimos mientras se cumpla una condición
- Depende de una condición True/False.
- Necesita controlar la condición para evitar un bucle infinito
- Ideal cuando no sabemos exactamente cuántas repeticiones habrá.

"""
#CON FOR
# for num in range(1,11):
#     print(num)
#CON WHILE    
# numero = 1
# while numero<=10:
#     print(numero) #Imprimir cunado sea V
#     numero +=1
# #Sumar cantidades y promedio
# suma = 0        
# contador = 0
# numero = float(input("Ingrese un numero 0 para terminar:"))
# while numero !=0:
#     suma += numero
#     contador += 1
#     numero = int(input("Ingrese un numero 0 para terminar:"))
#     if contador >0:
#         promedio = suma / contador 
#     else:
#         print("No se ingreso numeros")    
# print(f"Cantidad {contador}")        
suma = 0
contador = 0
continuar = "s"

while continuar == "s":
    numero = float(input("Ingrese un número: "))
    suma += numero
    contador += 1
    continuar = input("¿Desea continuar? (s/n): ").--
print("Suma total:", suma)
print("Cantidad de números:", contador)