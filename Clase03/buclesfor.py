"""El Bucle For es un proceso repetitivo
que me permite iterar n veces de acuerdo
al rango que le indique
for <variable> in range(ini,fin,salto)
"""
#Mostrar Hola Mundo 5 veces
#for _ in range(5):
#    """CUERPO DEL BUCLE"""
#    print("Hola Mundo")
#Mostrar numeros del 1 20
#for num in range(1,21):
#    print(num)
#texto = "Aprendiendo Python en SENATI"
#for letra in texto:
#    print(letra)
#Estructura de datos Listas
#frutas = ["bananas","manzanas","peras"]
#for fruta in frutas:
#    print(fruta)
#for num in range(5,21,2):
#    print(num)        
# for num in range (1,11):
#     if num==5:
#         break #interrumpir el bucle
#     else:
#         print(num)
# for num in range(1,11):
#     if num==5:
#         continue
#     else:
#         print(num)        
"""
Ingresar 5 empleados con su sueldo bruto
calcular:
- El Total de la planilla
- El Promedio total 
"""    
tot = 0
emp = 0
for trab in range(1,6):
    sueldo = float(input(f"Sueldo {trab}:"))
    tot += sueldo #tot=tot+sueldo
    emp += 1 #emp=emp+1
promedio= tot / emp
print(f"El Total de sueldo es {round(tot,2)}")    
print(f"El Promedio de sueldo es {round(promedio,2)}")

