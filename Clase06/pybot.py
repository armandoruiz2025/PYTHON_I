chatbot = {
    "hola": "¡Hola! ¿Cómo estás?",
    "como estas": "Estoy muy bien, gracias por preguntar",
    "como te llamas": "Me llamo PYBOT",
    "que puedes hacer": "Conversar contigo",
    "adios": "¡Hasta luego! Que tengas un buen día",
    "python":"claro puedo ayudarte en python"
}

print("🤖 PyBot: ¡Hola!")
print("Escribe 'adios' para terminar.")
while True:
    mensaje = input("Tú: ")
    if mensaje == "adios":
        print("🤖 PyBot:", chatbot["adios"])
        break
    elif mensaje in chatbot:
        print("🤖 PyBot:", chatbot[mensaje])
    else:
        print("🤖 PyBot: No entiendo tu mensaje")