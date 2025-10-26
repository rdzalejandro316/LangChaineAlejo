from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

# Ejemplo de tool simple
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# Crear el modelo Gemini
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant"
)


response = agent.invoke({"messages": [{"role": "user", "content": "what is the weather in Bogotá"}]})
print(response)
