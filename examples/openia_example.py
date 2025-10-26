from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

# Verifica que la variable esté disponible
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la variable OPENAI_API_KEY en el entorno")

# Crear cliente con la clave cargada
client = OpenAI(api_key=api_key)

print("Creating a response using the OpenAI API...")

response = client.responses.create(
    model="gpt-4o-mini",
    input="Tell me a three sentence bedtime story about a unicorn."
)

print(response.output_text)
