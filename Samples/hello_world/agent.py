from google.adk.agents.llm_agent import Agent
from typing import Dict, Any
import random
from reportlab.pdfgen import canvas


#First tool
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


# 2nd Tool

def generate_pdf_report(content: str) -> Dict[str, str]:
    """
    Generates a simple PDF report from provided text content.
    """
    filename = "research_report.pdf"
    pdf = canvas.Canvas(filename)
    pdf.setFont("Helvetica", 12)

    y = 800  # Start near top of page
    for line in content.split("\n"):
        pdf.drawString(40, y, line)
        y -= 15  # simple line spacing

    pdf.save()
    return {"pdf_path": filename}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful research assistant that user questions.',
    instruction=(
        "You are a Research Helper Agent. Answer clearly using your knowledge. "
        "Use search_topic(topic) for topics "
        "or when the user asks for facts, summaries, or explanations. "
        "If unknown, answer with general reasoning. "
        "Always provide a clear, readable summary."
        "If the user's request contains the word 'pdf', call generate_pdf_report(content) after summarizing.\n"
    ),
    tools=[search_topic, generate_pdf_report],
)
