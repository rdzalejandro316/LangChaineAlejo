# LangGraph Project

Este proyecto es una implementación práctica que demuestra el uso integrado de LangChain y LangGraph para crear aplicaciones de procesamiento de lenguaje natural avanzadas.

## Descripción

Este proyecto sirve como ejemplo práctico para entender y trabajar con:
- **LangChain**: Framework para desarrollar aplicaciones impulsadas por modelos de lenguaje
- **LangGraph**: Herramienta para crear flujos de trabajo con LLMs de manera estructurada

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Una cuenta y API key de Google para usar Gemini (si planeas usar los ejemplos de Gemini)

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/rdzalejandro316/LangChaineAlejo.git
cd LangChaineAlejo
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Configuración

1. Crea un archivo `.env` en la raíz del proyecto
2. Añade tus claves API según el modelo que vayas a utilizar:
```env
GOOGLE_API_KEY=tu_clave_api_de_google
```

## Uso

Para ejecutar el agente de LangGraph:
```bash
uv run langgraph dev
```

