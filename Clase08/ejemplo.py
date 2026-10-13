"""
Crear un progama que permita ingresar dos fechas y
Calcular cuantos dias y semanas hay entre ellas utilize
El Modulo datetime
"""
from datetime import datetime
fecha1 = input("Ingrese la primera fecha (dd/mm/aaaa):")
fecha2 = input("Ingrese la segunda fecha (dd/mm/aaaa):")
f1 = datetime.strptime(fecha1,"%d/%m/%Y")
f2 = datetime.strptime(fecha2,"%d/%m/%Y")
diferencia = abs(f2 - f1)
dias = diferencia.days
semanas = dias//7
dias_restantes = dias % 7
print(f"Los dias trabajado {dias}")
print(f"Las semanas trabajadas {semanas}")
print(f"Los dias restantes {dias_restantes}")
