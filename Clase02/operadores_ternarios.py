"""
resultado = valor_si_verdadero if condicion else valor_si_falso
"""
edad =17
mensaje="mayor de edad" if edad>=18 else "menor de edad"
print(mensaje)

nota=11
resultado = "Aprobado" if nota>=11 else "Desaprobado"
print(resultado)

compra = 600
descuento = compra * 0.15 if compra>=500 else 0
print(descuento)

"""
Para comenzar, recomiendo usar ternarios cuando hay 
solo dos resultados posibles .Para varias condiciones 
normalmente use if / elif / else mas claro
"""