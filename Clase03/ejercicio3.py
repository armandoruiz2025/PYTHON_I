productos = ["Laptop", "Mouse", "Teclado", "USB", "Monitor", "Celular"]
"""Si el producto es "USB", utiliza continue para ignorarlo. 
Si encuentras "Monitor", muestra "Producto encontrado: Monitor" y utiliza --break. 
Para los demás productos, muestra "Procesando: [producto]".
"""
for producto in productos:
    if producto=="USB":
        continue
    if producto=="Monitor":
        print(f"Producto Encontrado {producto}")
        #continue
        break
    print(f"Procesando...{producto}")