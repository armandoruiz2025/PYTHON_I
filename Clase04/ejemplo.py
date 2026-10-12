"""
Estructura de Datos
LISTAS .- mutables
"""

notas = [] #inicializando las listas
notas = list() #Constructor
"""
La funcion append me permite añadir elementos
al final del la lista
"""
while True:
    nota = float(input("Ingrese la calificacion:"))
    notas.append(nota)
    continuar = input("Desea continuar? (si/no)")
    if continuar.lower()=="no":
        break #FALSE
promedio = sum(notas)/len(notas)    
print(f"El Promedio del aula es {round(promedio,2)}")

