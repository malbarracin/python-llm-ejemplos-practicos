import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Few-shot examples en mensajes anteriores
messages = [
    {"role": "system", "content": "Eres un asistente experto en tecnología que responde con definiciones cortas y claras."},
    {"role": "user", "content": "¿Qué es una API REST?"},
    {"role": "assistant", "content": "Una API REST es una interfaz que permite comunicación entre sistemas usando HTTP y recursos identificados por URLs."},
    {"role": "user", "content": "¿Qué es Docker?"},
    {"role": "assistant", "content": "Docker es una plataforma que permite empaquetar, distribuir y ejecutar aplicaciones en contenedores livianos y aislados."},
    {"role": "user", "content": "¿Qué es Kubernetes?"},
]

respuesta = client.chat.completions.create(
    model="gpt-4-turbo",
    temperature=0.7,
    messages=messages,
)

# Imprime la respuesta generada por el modelo
print("🔹 Respuesta con ejemplos few-shot:\n", respuesta.choices[0].message.content)
