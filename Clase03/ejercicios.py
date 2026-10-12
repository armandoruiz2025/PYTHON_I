numeros = [10, 25, 8, 40, 15, 30, 50]
for num in numeros:
    if num <10:
        continue
    print(f"Revisando {num}")
    if num ==40:
        print(f"Numero encontrado {num}")
        break
   