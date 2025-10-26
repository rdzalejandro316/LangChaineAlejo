import google.generativeai as genai
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Configurar API Key desde entorno
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# Enviar un prompt
response = model.generate_content("Dame un ejemplo de hola mundo en python.")

# Mostrar respuesta
print(response.text)
