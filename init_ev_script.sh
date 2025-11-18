# Instalar uv (en windows)
pip install uv

# Iniciar un nuevo proyecto
uv init myproject
cd myproject

# Añadir dependencias
uv add requests flask

# Crear / sincronizar entorno virtual
uv sync

# Ejecutar un script
uv run script.py

#especificar versión de python
uv python install 3.12
uv sync --python 3.12

# en un proyecto existente
uv init .
uv pip install -r requirements.txt

# run the agent
uv run langgraph dev