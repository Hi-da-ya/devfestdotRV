# Challenge: Build Your First Tool – `search_topic`
Now that your environment is ready and your first agent is running, it's time to build your **first custom tool**.


## Concept
As powerful as they are, LLMs used in *isolation* have some key limitations. For example, their knowledge is frozen at the time they were trained - and they cannot interact directly with the outside world.

A key development that enables a more dynamic approach is 'tool calling'. Here's how it works:

*   With each request, you provide the LLM with a list of available tools and their descriptions.
*   The LLM uses these descriptions to decide which tool (if any) can help fulfill the request.
*   Instead of running the tool itself, the LLM generates a structured output that specifies which tool it wants to use and what information to pass to it.
*   Your application code receives this output, executes the actual tool, and then calls the LLM a second time, providing the tool's result as part of the new request.
*   The LLM then uses the tool's output to generate its final response to you.


## Task
In this lesson, you will create a simple tool called **`search_topic`**.  
When a user asks the agent about a topic, the agent will call this tool, fetch a summary, and return it in a clean, readable format.

### **1. Create the tool function**

Inside your agent file, add:

```python
    def search_topic(topic:str) -> Dict[str, Any]:
    """
    Return a short summary + 3 key facts for a topic from the sample db.
    """
    sample_db = {
        "climate change": {
            "definition": "Climate change is the long-term alteration of Earth's climate due to human and natural factors.",
            "facts": [
                "Global temperatures have risen by about 1.2°C since the late 1800s.",
                "Human activities like burning fossil fuels drive climate change.",
                "Sea levels are rising due to melting glaciers and ice sheets.",
                "Climate change increases extreme weather events.",
                "Renewable energy reduces carbon emissions."
            ]
        },

        "mental health": {
            "definition": "Mental health refers to emotional, psychological, and social well-being.",
            "facts": [
                "Regular exercise reduces stress and boosts mood.",
                "Anxiety disorders are the most common mental health condition globally.",
                "Stigma prevents many from seeking help.",
                "Early intervention improves long-term outcomes.",
                "Maintaining social connections supports mental health."
            ]
        },

        "digital safety": {
            "definition": "Digital safety is the practice of protecting your devices, data, and privacy online.",
            "facts": [
                "Strong passwords reduce the risk of hacking.",
                "Phishing is the most common cyberattack.",
                "Using two-factor authentication improves security.",
                "Public Wi-Fi increases data exposure risk.",
                "Software updates patch vulnerabilities."
            ]
        }
    }

    topic_lower = topic.lower().strip()
    for key in sample_db:
        if key in topic_lower:
            data = sample_db[key]
            facts_text = "\n".join(f"- {f}" for f in data["facts"][:3])
            return {
                "topic": key,
                "summary": f"{key.title()} is: {data['definition']}\n\nKey facts:\n{facts_text}"
            }

    rng = random.Random(topic_lower)
    facts = [
        f"{topic.title()} {rng.choice(['impacts our daily lives', 'is studied worldwide', 'has multiple dimensions'])}.",
        f"{topic.title()} is {rng.choice(['important', 'interesting', 'emerging'])}.",
        f"Researchers have found insights about {topic.lower()}."
    ]

    return {
        "topic": topic_lower,
        "summary": f"{topic.title()} is an interesting topic.\n\nKey facts:\n- " + "\n- ".join(facts)
    }
```
### 2. Register the tool with your agent

Add the function to your agent like this:
```python
root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful research assistant.',
    instruction=(
        "You are a Research Helper Agent. "
        "Use search_topic(topic) for topics or when the user asks for facts or summaries."
    ),
    tools=[search_topic]
)
```

### 3. Start the Developer UI:

```bash
adk web
```

### 4. Try in the UI:
- Give me facts about climate change

## Outcome
You'll see the `search_topic` function being called by your agent when you for fact-based questions, and the Dev UI will display the function call details in the Trace view.

  
