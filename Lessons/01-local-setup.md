# Lesson: Local Setup & Your First Agent
Welcome to the start of your AI agent journey!  
Let's set up your local environment and run your very first agent using the Google Agent Developer Kit (ADK).

---

## Concept
Before we build tools or customize agent behavior, we need to get your development environment ready.

In this Lesson, you will:
- Set up Python and a virtual environment  
- Install the Agent Developer Kit (ADK)  
- Generate a starter agent project  
- Launch the ADK Developer UI and interact with your agent  

This step helps you understand **how agents run**, **how the UI works**, and where your code fits in the bigger workflow.

---

## Prerequisites
Make sure you have:
- **Python 3.10+** installed  
- Comfort using a terminal  
- Internet connection for installing packages  

*(If you're on Ubuntu, Python usually comes installed already.)*

---

## Task

### **1. Create a project folder**
```bash
mkdir ai-agent-workshop
cd ai-agent-workshop
```

### **2. Create and activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS

venv\Scripts\activate # Windows
```

### **3.  Install the Google Agent Developer Kit**
```bash
pip install google-adk
```
This gives you the adk command-line tool and all the libraries needed to build agents.

### **4. Generate a starter agent**
1. Create a new ADK project:
   ```bash
   adk create demo
   ```

2. Start the Developer UI:
   ```bash
   adk web
   ```

### Outcome
You should now have the ADK Developer UI running locally at:
```
http://localhost:8000
```

From here you can:
- Chat with your first agent
- Explore how it responds to prompts
- See the request/response flow in the Trace view

## Question
The `adk web` command starts a local web server.

Explore the UI tabs and answer:
- What does each of these tabs do? **Trace, Events, State, Artifacts, Sessions, Eval**
- Which one would be most useful for debugging tool calls?   