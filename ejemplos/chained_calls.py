import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

tema = "¿Qué es la computación cuántica?"

# Primera llamada: obtener explicación inicial
explicacion_inicial = client.chat.completions.create(
    model="gpt-4-turbo",
    temperature=0.7,
    messages=[
        {"role": "user", "content": f"Explica brevemente: {tema}"}
    ],
).choices[0].message.content

# Segunda llamada: obtener sugerencias de mejora
sugerencias = client.chat.completions.create(
    model="gpt-4-turbo",
    temperature=0.5,
    messages=[
        {"role": "system", "content": "Eres un editor experto en explicar conceptos complejos claramente."},
        {"role": "user", "content": f"Dame sugerencias concretas para mejorar esta explicación:\n{explicacion_inicial}"}
    ],
).choices[0].message.content

# Tercera llamada: obtener la versión final mejorada
explicacion_mejorada = client.chat.completions.create(
    model="gpt-4-turbo",
    temperature=0.5,
    messages=[
        {"role": "system", "content": "Utiliza las sugerencias proporcionadas para mejorar y aclarar la explicación original."},
        {"role": "user", "content": f"Explicación original:\n{explicacion_inicial}\n\nSugerencias de mejora:\n{sugerencias}\n\nEscribe ahora una explicación mejorada en un párrafo breve."}
    ],
).choices[0].message.content

# Mostrar resultados encadenados
print("🔸 Explicación inicial:\n", explicacion_inicial, "\n")
print("🔹 Sugerencias de mejora:\n", sugerencias, "\n")
print("✅ Explicación mejorada:\n", explicacion_mejorada)
