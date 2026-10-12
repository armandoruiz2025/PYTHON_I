# for i in range(1,6):
#     print(i)
# else:
#     print("El Recorrido ok")  
# numeros = [10,20,30,40,50]
# encontrado = False #FLAG
# for numero in numeros:
#     if numero == 50:
#         encontrado=True
#         break
# if encontrado: #ESTO SE REALIZADA CUANDOA VARIABLE ES TRUE
#      print("EXITO")
# else:
#     print("NO EXITO")

encontrado = False
alumnos = ["Magaly","Maria","Oscar","Domini","Luis"]
alumno = input("Ingrese el alumno a buscar:")
for alu in alumnos:
    if alumno==alu:
        encontrado=True
        break
if encontrado:
    print("Alumno en clase")    
else:
    print("Alumno aun no esta en clase")    
    
