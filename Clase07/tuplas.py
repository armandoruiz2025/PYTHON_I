"""
- Es un tipo de estructura de datos (permite guardar varios
datos en una variable)
- Se define entre parentisis y se inicializa con tuple
- Es Ordenada
- Es Inmutable . unacez creada , no puedes agregar,eliminar,
ni reemplazar ningun elemento
- Su posicion empieza con 0
"""

valores = tuple()
valores = (12,34,56)
# valores.add(34)
# valores.pop(0)
# valores[0] = 23

"""
Se tiene los siguientes datos venidos
y almacenados en una tupla
poblacion = (27000,779999,4343434,434343)
por error se debe cambiar el ultimo valor
"""
poblacion=(27000,779999,4343434,434343)
"1 paso convertir de tuple a list"
lista_poblacion=list(poblacion)
"2 paso modificar el item existente"
lista_poblacion[3]=434373
"3 convertirlo a tupla nuevamente"
poblacion = tuple(lista_poblacion)
print(poblacion)