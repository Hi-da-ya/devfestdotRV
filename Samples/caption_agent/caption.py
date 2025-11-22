from google.adk.agents.llm_agent import Agent
from typing import Optional
from pydantic import BaseModel

# Tool Definition

class CaptionInput(BaseModel):
    raw: str
    tone: Optional[str] = "warm"
    platform: Optional[str] = "instagram"
    length: Optional[str] = "medium"


def craft_caption(input: CaptionInput) -> str:
    text = input.raw.strip()
    # Basic cleanup
    text = " ".join(text.split())

    tone = input.tone.lower()
    platform = input.platform.lower()
    length = input.length.lower()

    caption = text

    # Length handling
    if length == "short":
        if len(caption) > 80:
            caption = caption[:75].rsplit(" ", 1)[0] + "…"

    elif length == "long":
        caption = (
            caption
            + "\n\n"
            + "Sometimes you just need space to say it fully — and that’s okay."
        )

    # Tone adjustments
    if tone == "professional":
        caption = caption.replace("I'm", "I am").replace("don't", "do not")

    if tone == "emotional":
        caption += " ❤️"

    # Platform adaptations
    if platform == "linkedin":
        caption = caption.replace("gonna", "going to").replace("wanna", "want to")

    if platform == "instagram":
        caption += "\n\n✨"

    if platform == "tiktok":
        caption = caption.lower()

    return caption


# Agent Definition


root_agent = Agent(
    model="gemini-2.5-flash",
    name="caption_agent",
    description="An agent that transforms raw thoughts into meaningful social media captions.",
    instruction=(
        "You are Caption Crafter — an agent that turns raw, unstructured thoughts into "
        "clean, warm, meaningful social media captions.\n\n"

        "Your style:\n"
        "- warm, clear, relatable\n"
        "- never cliché\n"
        "- emotionally aware\n"
        "- concise but meaningful\n\n"

        "Your job:\n"
        "- Understand the emotion behind the raw input\n"
        "- Transform it into a polished caption\n"
        "- Match tone + platform if provided\n"
        "- Offer variations only when asked\n"
        "- Avoid over-motivation unless the user wants it\n"
        "- Keep the human voice alive\n\n"

        "If the user gives extremely short text, expand it thoughtfully.\n"
        "If the user gives long chaotic text, compress it without losing the message.\n"
    ),
    tools=[craft_caption],
)
