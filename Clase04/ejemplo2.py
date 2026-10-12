clave_correcta = "python123"
intentos = 1
while intentos <=3:#Cuando sea Verdadero
    clave = input("Ingrese contraseña:")
    if clave==clave_correcta:
        print("Acceso Permitido")
        break
    print("Contraseña Incorrecta")
    intentos +=1
else:
    print("Se agotaron los intentos")
