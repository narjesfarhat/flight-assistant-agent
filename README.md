# ✈️ Flight Assistant AI Agent

An intelligent tool-using flight assistant built with **LangGraph**, powered locally by **Ollama**, and deployed through an interactive **Gradio** chat interface.

This project demonstrates how modern AI agents can reason, choose tools, and complete real-world tasks such as searching flights, booking tickets, and handling customer complaints — all without relying on paid APIs.

---

## 🚀 Features

✅ **ReAct-style AI Agent** using LangGraph
✅ **Runs Fully Local** with Ollama (`qwen2.5:3b`)
✅ **Interactive Gradio Chat UI**
✅ **Tool Calling Capabilities**
✅ **Conversation Memory Support**
✅ **Deterministic Responses** (`temperature=0.3`)
✅ Clean and extendable architecture

---

## 🧠 What This Agent Can Do

### 🔍 Search Flights

Find available flights between two destinations with time and pricing.

### 🎫 Book Tickets

Generate booking confirmations for passengers instantly.

### 📝 Submit Complaints

Save passenger complaints into text files for review.

---

## 🧩 How It Works

This project uses a **ReAct Agent Architecture**, meaning the AI can:

1. Understand the user's request
2. Decide whether a tool is needed
3. Use the correct tool
4. Return a helpful final answer

This makes the assistant more reliable, useful, and realistic than a normal chatbot.

---

## 🛠 Tech Stack

* **Python 3.10+**
* **LangGraph**
* **LangChain Core**
* **Ollama**
* **Gradio**
* **Qwen 2.5 3B**
* **Local AI Inference**

---

## 📦 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/flight-assistant-agent.git
cd flight-assistant-agent
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Environment

**Windows PowerShell**

```bash
.\venv\Scripts\Activate.ps1
```

**Git Bash**

```bash
source venv/Scripts/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Pull Ollama Model

```bash
ollama pull qwen2.5:3b
```

---

## ▶️ Run The App

```bash
python app.py
```

Gradio will launch automatically in your browser.

---

## 📁 Project Structure

```bash
flight-assistant-agent/
│── app.py
│── requirements.txt
│── README.md
│── complaints/
```

---

## 💡 Example Prompts

* Find flights from Cairo to Dubai on 2026-07-10
* Book GA101 for John Smith
* My baggage was lost and I want to submit a complaint
* Show me the cheapest available flight

---

## 🔥 Why This Project Matters

This project showcases practical skills in:

* AI Agents
* Tool Calling
* Local LLM Deployment
* Python Backend Logic
* UI Deployment with Gradio
* LangChain / LangGraph Ecosystem

Strong portfolio project for **AI Engineer / Python Developer / Automation roles**.

---

## 🤝 Contributing

Pull requests are welcome.
For major improvements, open an issue first to discuss ideas.

---

## 📜 License

MIT License

---

## ⭐ Acknowledgements

* LangGraph for agent orchestration
* Ollama for local LLM serving
* Gradio for rapid UI deployment
* Qwen Team for the language model

---

## 👨‍💻 Author

Built with ambition, curiosity, and real engineering focus.

