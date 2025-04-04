import os
from openai import OpenAI, AzureOpenAI
from dotenv import load_dotenv
import azure.identity

# Setup the OpenAI client to use either Azure, OpenAI.com, or Ollama API
load_dotenv(override=True)

# Configuración del cliente según el proveedor
API_HOST = os.getenv("API_HOST", "github")

if API_HOST == "azure":
    token_provider = azure.identity.get_bearer_token_provider(
        azure.identity.DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
    )
    client = AzureOpenAI(
        api_version=os.environ["AZURE_OPENAI_VERSION"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        azure_ad_token_provider=token_provider,
    )
    MODEL_NAME = os.environ["AZURE_OPENAI_DEPLOYMENT"]
elif API_HOST == "ollama":
    client = OpenAI(base_url=os.environ["OLLAMA_ENDPOINT"], api_key="nokeyneeded")
    MODEL_NAME = os.environ["OLLAMA_MODEL"]
elif API_HOST == "github":
    client = OpenAI(base_url="https://models.inference.ai.azure.com", api_key=os.environ["GITHUB_TOKEN"])
    MODEL_NAME = os.getenv("GITHUB_MODEL", "gpt-4o")
else:
    client = OpenAI(api_key=os.environ["OPENAI_KEY"])
    MODEL_NAME = os.environ["OPENAI_MODEL"]

tema = "¿Qué es la computación cuántica?"

# Primera llamada: obtener explicación inicial
explicacion_inicial = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.7,
    messages=[
        {"role": "user", "content": f"Explica brevemente: {tema}"}
    ],
).choices[0].message.content

# Segunda llamada: obtener sugerencias de mejora
sugerencias = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.5,
    messages=[
        {"role": "system", "content": "Eres un editor experto en explicar conceptos complejos claramente."},
        {"role": "user", "content": f"Dame sugerencias concretas para mejorar esta explicación:\n{explicacion_inicial}"}
    ],
).choices[0].message.content

# Tercera llamada: obtener la versión final mejorada
explicacion_mejorada = client.chat.completions.create(
    model=MODEL_NAME,
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
