import os
import tiktoken
from dotenv import load_dotenv

# Carga las variables de entorno
load_dotenv(override=True)

# Configuración según el proveedor
API_HOST = os.getenv("API_HOST", "github")

# Seleccionar el modelo según el proveedor
if API_HOST == "azure":
    MODEL_NAME = os.environ["AZURE_OPENAI_DEPLOYMENT"]
elif API_HOST == "ollama":
    MODEL_NAME = os.environ["OLLAMA_MODEL"]
elif API_HOST == "github":
    MODEL_NAME = os.getenv("GITHUB_MODEL", "gpt-4o")
else:
    MODEL_NAME = os.environ["OPENAI_MODEL"]

# Texto de ejemplo
texto = "La inteligencia artificial está revolucionando el mundo."

try:
    # Intentar obtener el codificador específico para el modelo
    encoding = tiktoken.encoding_for_model(MODEL_NAME)
    print(f"\n🔵 Usando codificador para modelo {MODEL_NAME}")
except KeyError:
    # Si el modelo no tiene un codificador específico, usar el codificador por defecto
    encoding = tiktoken.get_encoding("cl100k_base")
    print(f"\n🔵 Usando codificador por defecto cl100k_base para {MODEL_NAME}")

# Tokenizar el texto
tokens = encoding.encode(texto)

print("\n📑 Texto original:", texto)
print("📊 Número de tokens:", len(tokens))
print("📃 Tokens generados:", tokens)

# Decodificar nuevamente los tokens a texto
texto_decodificado = encoding.decode(tokens)
print("✅ Texto decodificado:", texto_decodificado)