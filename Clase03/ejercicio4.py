"""
Ejercicio 3: Sueldos y aumento salarial
Una empresa tiene los siguientes sueldos:
sueldos = [1200, 1600, 1800, 2100, 2500, 2800, 3200, 4000]
Crea un programa que recorra la lista y:
•	Utilice un acumulador para calcular el total de sueldos. 
•	Utilice un contador para contar los trabajadores que ganan menos de 2000. 
•	Utilice continue para ignorar los sueldos menores a 1300. 
•	A los trabajadores que ganen entre 2000 y 3000, aplicarles un aumento del 10%. 
•	Si encuentra un sueldo de 4000, detener el recorrido utilizando break. 
"""
sueldos = [1200, 1600, 1800, 2100, 2500, 2800, 3200, 4000]
cant_sueldos=0
menos_2000=0
dosatres=0
totsue=0
for sueldo in sueldos:
    totsue += sueldo
    cant_sueldos +=1
    if sueldo<1300:
        continue
    elif sueldo<2000:
        menos_2000 += 1
    elif 3000>=sueldo and sueldo>=2000:
        sueldo = (sueldo * 0.1) + sueldo
    elif sueldo== 4000:
        print(sueldo)
        break
    #print(sueldo)
print(f"La cantidad de sueldos calculados son {cant_sueldos}")
print(f"La cantidad de trabajadores que ganan menos de 2000 soles son {menos_2000}")
