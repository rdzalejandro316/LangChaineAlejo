from langchain_core.messages import AIMessage, SystemMessage
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class State(MessagesState):
    customer_name: str
    my_age: int

state: State = {}
customer_name = state.get("customer_name", None)
print(customer_name)

def node_1(state: State):
    new_state: State = {}
    if state.get("customer_name") is None:
        new_state["customer_name"] = "John Doe"
    else:
        new_state["my_age"] = 20

    history = state.get("messages", [])
    
    # Solo invocar el LLM si hay mensajes en el historial
    if history:
        # Agregar mensaje de sistema al principio si no existe
        messages = [SystemMessage(content="You are a helpful assistant")] + history
        print("*********************************:", messages)
        ai_message = llm.invoke(messages)
        new_state["messages"] = [ai_message]
    
    return new_state

builder = StateGraph(State)
builder.add_node("node_1", node_1)

builder.add_edge(START, 'node_1')
builder.add_edge('node_1', END)

agent = builder.compile()