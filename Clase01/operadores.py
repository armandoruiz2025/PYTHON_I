"""
OPERADORES ARITMETICOS
Operador	Operación	Ejemplo	Resultado
+	          Suma	     5 + 2	     7
-	          Resta	     5 - 2	     3
*	          Multi	     5 * 2	    10
/	          Divi	     5 / 2	    2.5
//	          DiviEnt	 5 // 2	      2
%	          Mód 	     5 % 2	      1
**	          Potenc	 5 ** 2	     25
"""
print('HOLA DESDE PYTHON')
print("YA SE EJECUTAR UN PROGRAMA EN PYTHON")
#OPERADOR COMA SIRVE PARA CONCATENAR
print("SUMA",5 + 2)
print("RESTA",5 - 2)
print("MULTI",5 * 2)
print("DIV ENT", 5 // 2)
print("DIV DEC", 5 / 2)
print("MODULO", 5 % 2)

nombre = "Magaly"
apellido = "Gomez"
edad = 20
nombrecompleto = nombre + apellido
print(nombre,apellido)
print(nombrecompleto)
#concatenar cadenas con f-strings
print(f"Su nombre:{nombre} y a su apellido{apellido} y su edad {edad}")
print(f"Su nombre: {nombre} y su apellido: {apellido}\n"
      f"Su edad: {edad}")

