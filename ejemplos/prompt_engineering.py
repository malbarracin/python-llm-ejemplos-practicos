import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Prompt simple vs Prompt específico
prompt_simple = "Dame ideas sobre inteligencia artificial."
prompt_especifico = (
    "Eres un experto en IA generativa. "
    "Dame 3 ideas concretas de proyectos de inteligencia artificial aplicados a la medicina, "
    "en formato de lista numerada."
)

def obtener_respuesta(prompt):
    respuesta = client.chat.completions.create(
        model="gpt-4-turbo",
        temperature=0.7,
        messages=[{"role": "user", "content": prompt}],
    )
    return respuesta.choices[0].message.content

# Resultado prompt simple
resultado_simple = obtener_respuesta(prompt_simple)
print("🔸 Respuesta con prompt simple:\n", resultado_simple, "\n")

# Resultado prompt específico
resultado_especifico = obtener_respuesta(prompt_especifico)
print("🔹 Respuesta con prompt específico:\n", resultado_especifico)
