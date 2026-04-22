# ✈️ Flight Assistant AI Agent  
A tool‑using AI agent built with **LangGraph**, powered by a local **Ollama** model, and served through a **Gradio** chat interface.  
The agent can search flights, book tickets, and save passenger complaints using custom Python tools.

---

## 🚀 Features
- **ReAct‑style AI agent** using LangGraph  
- **Local LLM** via Ollama (no API key required)  
- **Three custom tools**:
  - Search available flights  
  - Book a flight for a passenger  
  - Save a complaint to a text file  
- **Gradio chat UI** for a clean, interactive experience  
- **Full conversation history** passed to the agent  
- **Deterministic responses** with low‑temperature settings  

---

## 🧠 Tech Stack
- **Python 3.10+**
- **LangGraph**
- **LangChain Core**
- **Ollama (local model: qwen2.5:3b)**
- **Gradio**
- **ReAct agent architecture**

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/flight-assistant-agent
cd flight-assistant-agent
2. Create a virtual environment
bash
python -m venv venv
3. Activate it
PowerShell

bash
.\venv\Scripts\Activate.ps1
Git Bash

bash
source venv/Scripts/activate
4. Install dependencies
bash
pip install -r requirements.txt
5. Pull the model
bash
ollama pull qwen2.5:3b
▶️ Run the App
bash
python app.py
Gradio will open in your browser automatically.

🛠 Tools Overview
🔍 search_flights
Returns a list of available flights between two cities.

🎫 book_flight
Generates a booking confirmation with a random ID.

📝 submit_complaint
Saves a passenger complaint to a .txt file.

🧩 Agent Architecture
This project uses LangGraph’s prebuilt ReAct agent, which:

Reads the user message

Decides whether a tool is needed

Executes the tool

Returns the final answer

This makes the agent reliable, explainable, and easy to extend.

📁 Project Structure
Code
flight-assistant-agent/
│
├── app.py               # Main application
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
└── complaints/          # Saved complaint files
🤝 Contributing
Pull requests are welcome.
For major changes, please open an issue first to discuss what you’d like to improve.

📜 License
MIT License

⭐ Acknowledgements
LangGraph for the agent framework

Ollama for local model hosting

Gradio for the UI