"""
Un diccionario es una estructura de datos 
que permite almacenar 
información mediante pares de clave : valor.
"""
alumnos = {
          "nombre":"Carlos",
          "apellido":"Gomez",
          "edad":19
          }
# print(alumnos["apellido"])
# print(alumnos["edad"])
# print(alumnos["nombre"])
# for clave,valor in alumnos.items():
#     print(f"{clave} - {valor}")

# for clave in alumnos.keys():
#     print(f"{clave}")

for valor in alumnos.values():
     print(f"{valor}")    
""""ITEMS .- ME PERMITE OBTENER LA CLAVE Y EL VALOR
KEYS.-ME DEVUELVE LA CLAVE DE UN ITEM
VALUES.-ME DEVUELVE EL VALOR DE UN ITEM
"""
