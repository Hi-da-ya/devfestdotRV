# Challenge: Build Your Second Tool – PDF Generation
Now that your agent can look up information using `search_topic`, let’s make it more powerful by adding a tool that can generate **PDF reports**.

This tool will allow the agent to take any text content and turn it into a downloadable PDF.  
Perfect for summaries, research notes, study guides, or workshop handouts.

---

## Concept
Your agent can already return answers in text form.  
But sometimes, the user wants the output as a **file** — especially something they can save, print, or share.

Tools give your agent abilities beyond text, and generating a PDF is a perfect example of this.

In this challenge, you will:
- Build a PDF generator tool using `reportlab`
- Connect it to your agent
- Trigger the tool when a user mentions “pdf”
- Test the full flow in the ADK UI

---

## Task

### **1. Install the ReportLab library**
If you haven’t already installed it:

```bash
pip install reportlab
```

### **2. Create the generate_pdf_report tool**
Add this function to your tools file or your agent file:

```python
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
```
This tool:
* Creates a file called research_report.pdf
* Writes each line of text onto the PDF
* Returns the file path for the user to download

### 3. Register the tool with your agent

Add the function to your agent like this:
```python
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
```

### 4. Start the Developer UI:

```bash
adk web
```

### 5. Try in the UI:
Make a pdf about digital safety

## Question
What guidelines help the LLM reliably choose between overlapping tools? How can you improve routing with clearer names, argument schemas, and examples?