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
    model=MODEL_NAME,
    temperature=0.7,
    messages=messages,
)

# Imprime la respuesta generada por el modelo
print("🔹 Respuesta con ejemplos few-shot:\n", respuesta.choices[0].message.content)
