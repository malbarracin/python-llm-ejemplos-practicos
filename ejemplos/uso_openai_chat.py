import os
from openai import OpenAI, AzureOpenAI
from dotenv import load_dotenv
import azure.identity

# Carga las variables de entorno
load_dotenv(override=True)

# Configuración del modelo según el proveedor
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

# Define la pregunta para el modelo
pregunta = "¿Cuál es el lenguaje de programación más popular en 2024?"

# Realiza la consulta al modelo GPT-4
respuesta = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.5,
    messages=[
        {"role": "system", "content": "Eres un asistente experto en tecnología y programación."},
        {"role": "user", "content": pregunta},
    ],
)

# Muestra la respuesta del modelo
print("Pregunta:", pregunta)
print("Respuesta del modelo:", respuesta.choices[0].message.content)
