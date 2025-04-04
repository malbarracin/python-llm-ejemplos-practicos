import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOllama

# Carga las variables de entorno
load_dotenv(override=True)

# Configuración del modelo según el proveedor
API_HOST = os.getenv("API_HOST", "github")

if API_HOST == "azure":
    llm = AzureChatOpenAI(
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        openai_api_version=os.environ["AZURE_OPENAI_VERSION"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    )
elif API_HOST == "ollama":
    llm = ChatOllama(
        base_url=os.environ["OLLAMA_ENDPOINT"],
        model=os.environ["OLLAMA_MODEL"]
    )
elif API_HOST == "github":
    llm = ChatOpenAI(
        model=os.getenv("GITHUB_MODEL", "gpt-4o"),
        openai_api_base="https://models.inference.ai.azure.com",
        openai_api_key=os.environ["GITHUB_TOKEN"]
    )
else:
    llm = ChatOpenAI(
        model=os.environ["OPENAI_MODEL"],
        openai_api_key=os.environ["OPENAI_KEY"]
    )

# Define un prompt usando Langchain
prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un experto en desarrollo de software, especialmente en Python."),
    ("user", "{input}")
])

# Crear una cadena (Chain) de Langchain combinando prompt y modelo
chain = prompt | llm

# Ejecutar la consulta
respuesta = chain.invoke({"input": "¿Qué es el patrón Singleton en programación?"})

# Mostrar resultado
print("🔹 Respuesta usando Langchain:\n", respuesta.content)
