"""
ESTRUCTURA DE DATOS .- ALMACENAR MAS DE UN DATO A LA VEZ.
- LISTAS [10,20,30...] LIST "MUTABLE"
- DICCIONARIOS {CLAVE:VALOR} DICT "MUTABLE"
- TUPLAS (10,20,30) TUPLE "INMUTABLES"
- CONJUNTOS {10,20,30} SET "MUTABLE"
"""
frutas = ["MANZANA","FRESA","UVA","ALBARICOQUE"]
#INSERTAR ELEMENTO A LA LISTA
frutas.append("GRANADILLA") #AL FINAL
frutas.insert(2,"PLATANO") #x POSICION
#ELIMINAR ELEMENTOS DE LA LISTA
frutas.pop(2) #x POSICION
frutas.remove("MANZANA") #POR EL ELEMENTO
#ACTUALIZAR UN ELEMENTO DE LA LISTA
frutas[0]="SANDIA" 
#ORDENAR LOS ELEMENTOS DE UNA LISTA
frutas.sort() #ORDENAR ASC
frutas.sort(reverse=True) #ORDENAR DESC
# for fruta in frutas:
#     print(fruta)

# numeros = [10,20,30,40,50,60,70]
# print(numeros[-1]) # 70  
# print(numeros[2:4]) #[30:40]
# print(numeros[:3]) #[10,20,30]

"""COMPRENSION DE LISTAS (comprehension)
Me permite crear una lista de forma
Mas corta usando un for y opcionalmente
Una Condicion
"""
# valores = [] #lista vacia
# for i in range(1,6):
#     valores.append(i)

#Comprension de listas
# numeros =[i for i in range(1,6)]
# print (numeros)

nombres = ["Ana", "Pedro", "Luis", "Alejandra", "José"]
nombres_largos = [nombre for nombre in nombres 
                  if len(nombre) > 4]
print(nombres_largos)

