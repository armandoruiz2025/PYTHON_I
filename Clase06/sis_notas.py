notas = {
    "Ana":[15,18,16],
    "Luis":[10,11,11],
    "Carlos":[12,8,7],
    "Maria":[2,17,20],
}
"""Mostrar el Alumno y sus notas
"""
for alumno,lista_notas in notas.items():
    promedio = sum(lista_notas) / len(lista_notas)
    print(f"{alumno} Promedio es: {round(promedio,2)}")
    rpta= "Aprobado" if promedio>=10 else "Desaprobado"
    print(rpta)        
