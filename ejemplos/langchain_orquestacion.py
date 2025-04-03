import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Carga las variables de entorno
load_dotenv()

# Define el modelo usando Langchain y OpenAI
llm = ChatOpenAI(model="gpt-4-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))

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
