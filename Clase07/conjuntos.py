"""
- No Permite Duplicados
- No Garantiza un orden de presentacion
- No Permite acceder mediante posicions como datos[0]
- Puedes Agregar y eliminar elementos
- No Puedes guarda listas ni diccionarios directamente
"""
#valores  = {20,15,34,78,15}
#print(valores)

alumnos = ["Diego","Oscar","Luis","Maria","Magaly","Maria"]
"""
Convirtiendo la lista a conjuntos
"""
alumnos_unicos = set (alumnos)
"Agregar"
alumnos_unicos.add ("Dominique") #Agrega un elemento
alumnos_unicos.update(["Manuel","Percy"]) #Agrega varios
"Eliminar "
alumnos_unicos.remove("Percy") #Elimina item - no error
alumnos_unicos.discard("Carlos") #Discard 
print(alumnos_unicos)