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

# Prompt simple vs Prompt específico
prompt_simple = "Dame ideas sobre inteligencia artificial."
prompt_especifico = (
    "Eres un experto en IA generativa. "
    "Dame 3 ideas concretas de proyectos de inteligencia artificial aplicados a la medicina, "
    "en formato de lista numerada."
)

def obtener_respuesta(prompt):
    respuesta = client.chat.completions.create(
        model=MODEL_NAME,
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
