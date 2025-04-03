import tiktoken

# Seleccionar el codificador específico para el modelo GPT-4
encoding = tiktoken.encoding_for_model("gpt-4")

# Texto de ejemplo
texto = "La inteligencia artificial está revolucionando el mundo."

# Tokenizar el texto
tokens = encoding.encode(texto)

print("Texto original:", texto)
print("Tokens generados:", tokens)

# Decodificar nuevamente los tokens a texto
texto_decodificado = encoding.decode(tokens)
print("Texto decodificado:", texto_decodificado)