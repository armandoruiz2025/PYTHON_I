"""
UNA FUNCION ES UN BLOQUE DE CODIGO QUE PERMITE
RETORNAR UNO O MAS VALORES.SE UTILIZA PARA REUTILIZAR
EL CODIGO.
"""
def saludo():
    print("Hola dese Python")

def mensaje(msj):
    rpta = f"hola {msj} ya leei tu mensaje"    
    return rpta

#print(mensaje("Jose"))
#saludo()

"""
Crear un programa que me permita ralizar
una calculadora basica. que me muestre un menu
de opciones
"""
def calculadora(num1,num2):
    print("Menu de Opciones")
    print("================")
    print("1.-Sumar")
    print("2.-Restar")
    print("3.-Multiplicar")
    print("4.-Dividir")
    print("5.-Salir")
    opc = input("Ingrese la opcion:(1-5):")
    if opc == "1":
        res = num1 + num2
    elif opc == "2":    
        res = num1 - num2
    elif opc == "3":    
            res = num1 * num2    
    elif opc == "4":    
            res = num1 / num2        
    else:
         res = "Adios"        
    return res     

def calculadora2(a,b):
    while True:
        print("\n1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir")
        op = input("Opción: ")
        if op == "5":
            break
        elif op == "1":
            res = a + b
        elif op == "2":
            res = a - b
        elif op == "3":
            res = a * b
        elif op == "4":
            res = a / b 
        else:
            print("Opción incorrecta")
            continue
        print("Resultado:", res)
        if input("¿Continuar (s/n)?: ").lower() == "n":
            break
calculadora2(12, 0)
# #print(calculadora(12,3))
