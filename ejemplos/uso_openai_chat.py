import os
from openai import OpenAI
from dotenv import load_dotenv

# Carga la API Key desde el archivo .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define la pregunta para el modelo
pregunta = "¿Cuál es el lenguaje de programación más popular en 2024?"

# Realiza la consulta al modelo GPT-4
respuesta = client.chat.completions.create(
    model="gpt-4-turbo",
    temperature=0.5,
    messages=[
        {"role": "system", "content": "Eres un asistente experto en tecnología y programación."},
        {"role": "user", "content": pregunta},
    ],
)

# Muestra la respuesta del modelo
print("Pregunta:", pregunta)
print("Respuesta del modelo:", respuesta.choices[0].message.content)
