"""
MATCH .- Utilizarlo >=3.7
"""
opcion = int(input("Ingrese la opcion:"))
match opcion:
    case 1:
        print("Elegistes Registrar")
    case 2:
        print("Elegistes Eliminar")    
    case 3:
        print("Elegistes Actualizar")    
    case _:
        print("Opcion Incorrecta")    