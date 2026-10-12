"""
Crea una lista de nombres:
nombres = ["Ana", "Pedro", "Luis", "Carlos", "María", "Juan"]
Recorre la lista utilizando for.
•	Si el nombre es "Luis", utiliza continue para no mostrarlo. 
•	Si encuentras "María", muestra "Encontramos a María" y utiliza break. 
•	Los demás nombres deben mostrarse normalmente.
"""

nombres = ["Ana", "Pedro", "Luis", "Carlos", "María", "Juan"]
for name in nombres:
    if name == "Luis":
        continue
    elif name == "María":
        print (f"{name}\nEncontramos a María")
        break
    print(name)