import json
import random
import string
from datetime import datetime
import gradio as gr
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

# LangChain 1.x no longer exports create_tool_calling_agent from langchain.agents
# Use langgraph's prebuilt react agent instead
from langgraph.prebuilt import create_react_agent

# ---------------- TOOLS ----------------

@tool
def search_flights(origin: str, destination: str, date: str) -> str:
    """Search available flights between two cities on a given date."""
    data = [
        {"flight": "GA101", "price": "$300", "time": "08:00"},
        {"flight": "GA202", "price": "$250", "time": "14:00"},
        {"flight": "GA303", "price": "$220", "time": "20:00"},
    ]
    return json.dumps(data, indent=2)

@tool
def book_flight(flight_number: str, passenger_name: str) -> str:
    """Book a specific flight for a passenger by name."""
    booking = "BK" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"Booking confirmed for {passenger_name}. Flight {flight_number}. ID: {booking}"

@tool
def submit_complaint(passenger_name: str, complaint_text: str) -> str:
    """Save a passenger complaint to a text file."""
    filename = f"{passenger_name.replace(' ', '_')}_complaint.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Passenger: {passenger_name}\n")
        f.write(f"Date: {datetime.now()}\n\n")
        f.write(complaint_text)
    return f"Complaint saved in {filename}"

tools = [search_flights, book_flight, submit_complaint]

# ---------------- MODEL ----------------

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.3
)

# ---------------- AGENT ----------------
# create_react_agent is the LangGraph replacement for create_tool_calling_agent + AgentExecutor

system_prompt = """You are a helpful Flight Assistant.
You can:
1. Search flights between cities
2. Book flights for passengers
3. Save passenger complaints to file
Use the provided tools whenever the user's request requires them."""

agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt=system_prompt
)

# ---------------- CHAT ----------------

# Gradio 4+ passes history as a list of dicts: [{"role": "user"/"assistant", "content": "..."}]
# (NOT as list of tuples anymore)

def chat(message: str, history: list) -> str:
    msgs = []

    for turn in history:
        if turn["role"] == "user":
            msgs.append(HumanMessage(content=turn["content"]))
        elif turn["role"] == "assistant":
            msgs.append(AIMessage(content=turn["content"]))

    result = agent.invoke({
        "messages": msgs + [HumanMessage(content=message)]
    })

    # The agent returns a list of messages; the last one is the AI reply
    return result["messages"][-1].content

# ---------------- UI ----------------

demo = gr.ChatInterface(
    fn=chat,
    title="✈️ Flight Assistant Agent",
    description="Search flights, book tickets, or submit complaints.",
    examples=[
        "Find flights from Cairo to Dubai on 2026-07-10",
        "Book GA101 for John Smith",
        "My name is Ahmed Ali and I want to complain about lost baggage"
    ]
)

demo.launch()