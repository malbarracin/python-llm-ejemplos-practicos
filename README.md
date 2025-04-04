# Python + IA: Ejemplos prácticos con Modelos de Lenguaje Grande (LLMs)

Este repositorio contiene ejemplos prácticos en Python para entender y utilizar los Modelos de Lenguaje Grande (LLMs), inspirados en conceptos avanzados de inteligencia artificial.

---

## 🚀 Tema 1: ¿Qué son los Modelos de Lenguaje Grande (LLMs)?

Los **Modelos de Lenguaje Grande (LLMs)** son modelos de inteligencia artificial basados en aprendizaje profundo (*deep learning*) capaces de comprender, generar y manipular el lenguaje humano. Algunos ejemplos populares de LLMs incluyen GPT-3.5, GPT-4 y LLaMA.

### ¿Cómo funcionan?

Un LLM funciona principalmente mediante un proceso llamado **predicción del siguiente token**. Esto significa que, dado un texto inicial (entrada), el modelo predice cuál es la palabra o token que probablemente vendrá a continuación, basándose en una distribución de probabilidad calculada internamente.

### Ejemplo práctico asociado:
- [Tokenización básica con tiktoken](ejemplos/llm_basico.py)

---

## 🚀 Tema 2: Uso práctico del LLM con Python (API de OpenAI)

Este ejemplo práctico muestra cómo interactuar fácilmente con la API de OpenAI desde Python utilizando la librería oficial `openai`. Aprenderás a realizar consultas rápidas al modelo y obtener respuestas sencillas.

### Ejemplo práctico asociado:
- [Uso básico del API ChatCompletion de OpenAI](ejemplos/uso_openai_chat.py)

---

## 🚀 Tema 3: Prompt Engineering

Aprende a formular instrucciones específicas para que los LLM generen respuestas más útiles y enfocadas.

### Ejemplo práctico asociado:
- [Prompt Engineering con OpenAI](ejemplos/prompt_engineering.py)

---

## 🚀 Tema 4: Ejemplos Few-shot

Aprende cómo utilizar ejemplos previos para guiar las respuestas de los modelos de lenguaje.

### Ejemplo práctico asociado:
- [Uso de Few-shot examples con OpenAI](ejemplos/few_shot_examples.py)

---


## 🚀 Tema 5: Llamadas Encadenadas (Chained Calls)

Aprende cómo realizar múltiples consultas consecutivas al modelo para mejorar progresivamente la calidad de las respuestas.

### Ejemplo práctico asociado:
- [Uso de llamadas encadenadas con OpenAI](ejemplos/chained_calls.py)

---


## 🚀 Tema 6: Librerías avanzadas para orquestación (Langchain)

Descubre cómo usar Langchain para integrar y orquestar modelos de lenguaje de forma sencilla y poderosa.

### Ejemplo práctico asociado:
- [Orquestación con Langchain y OpenAI](ejemplos/langchain_orquestacion.py)

---

## 📚 Temas Completados 🎉

- Tema 1: [¿Qué son los LLM? (Tokenización básica)](ejemplos/llm_basico.py)
- Tema 2: [Uso práctico del LLM con Python (API OpenAI)](ejemplos/uso_openai_chat.py)
- Tema 3: [Prompt Engineering](ejemplos/prompt_engineering.py)
- Tema 4: [Ejemplos Few-shot](ejemplos/few_shot_examples.py)
- Tema 5: [Llamadas encadenadas](ejemplos/chained_calls.py)
- Tema 6: [Librerías avanzadas para orquestación (Langchain)](ejemplos/langchain_orquestacion.py)

¡Ahora tienes una guía práctica completa para dominar los fundamentos esenciales sobre LLM con Python!

## 🛠️ Configuración del Proyecto

### Archivo .env

El proyecto soporta múltiples proveedores de LLM. Configura el archivo `.env` según el proveedor que desees usar:

```env
# Selecciona el proveedor (azure, ollama, github, openai)
API_HOST=github

# Configuración para Azure OpenAI
AZURE_OPENAI_ENDPOINT=https://YOUR-AZURE-OPENAI-SERVICE-NAME.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=YOUR-AZURE-DEPLOYMENT-NAME
AZURE_OPENAI_VERSION=2024-03-01-preview

# Configuración para Ollama
OLLAMA_ENDPOINT=http://localhost:11434/v1
OLLAMA_MODEL=llama2

# Configuración para OpenAI
OPENAI_KEY=YOUR-OPENAI-KEY
OPENAI_MODEL=gpt-3.5-turbo

# Configuración para GitHub Copilot
GITHUB_TOKEN=YOUR-GITHUB-TOKEN
GITHUB_MODEL=gpt-4o
```

### Proveedores Soportados

1. **Azure OpenAI**
   - Requiere una cuenta de Azure
   - Necesita configurar un recurso de Azure OpenAI
   - Mayor control y seguridad empresarial

2. **Ollama**
   - Opción gratuita y local
   - No requiere conexión a internet
   - Ideal para desarrollo y pruebas

3. **OpenAI**
   - API oficial de OpenAI
   - Requiere una cuenta y API key
   - Acceso a los últimos modelos

4. **GitHub Copilot**
   - Usa los modelos a través de GitHub
   - Requiere una cuenta de GitHub con acceso a Copilot
   - Buena opción para desarrollo

### Instalación

1. Clona el repositorio
2. Crea un archivo `.env` basado en el ejemplo anterior
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Uso

1. Configura el proveedor deseado en `.env` usando `API_HOST`
2. Asegúrate de tener las credenciales correctas para el proveedor seleccionado
3. Ejecuta cualquiera de los ejemplos:
   ```bash
   python ejemplos/uso_openai_chat.py
   ```

---

## Author
Marcelo Alejandro Albarracín
marceloalejandro.albarracin@gmail.com

## ¿Te gusta el contenido que comparto? Invítame un café para ayudarme a seguir creando. ¡Gracias por tu apoyo!
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-F7DF1E?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/malbarracin) 
