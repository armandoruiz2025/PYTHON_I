import math #Libreria importa funciones MAT
#import datetime #Libreria importa funciones FECHA
from datetime import datetime
"""VARLOR DE PI"""
print(math.pi)
"""RAIZ CUADRADA"""
print(math.sqrt(5))
"""FACTORIAL DE UN NUMERO"""
print(math.factorial(5))
"""ELIMINA DECIMALES"""
print(math.trunc(5.333))
#max(),min(),sum(),
"""FECHA Y HORA ACTUAL"""
#print(datetime.date.today())
ahora = datetime.now()
print(f"fecha {ahora}")
print(f"mes {ahora.month}")
print(f"dia {ahora.day}")
print(f"año {ahora.year}")