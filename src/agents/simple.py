from langchain_core.messages import AIMessage
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
agent = create_agent(
    model=llm,
    system_prompt="You are a helpful assistant"
)

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

    history = state["messages"]
    ai_message = agent.invoke({"messages": history})
    new_state["messages"] = [ai_message]
    return new_state

builder = StateGraph(State)
builder.add_node("node_1", node_1)

builder.add_edge(START, 'node_1')
builder.add_edge('node_1', END)

agent = builder.compile()