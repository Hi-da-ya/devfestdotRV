# A mock weather agent that gives weather conditions and facts of a city :-)

from google.adk.agents.llm_agent import Agent
from typing import Dict, Any, Optional
import random

def get_weather(city: str, date: Optional[str] = None) -> Dict[str, Any]:
    """
    Return a mock weather report (deterministic per city/date).
    """
    conditions = ["Sunny", "Cloudy", "Rainy", "Partly Cloudy", "Stormy", "Windy"]
    base_temps = {
        "Nairobi": 23,
        "Lagos": 28,
        "Cairo": 30,
        "Cape Town": 20,
        "Accra": 27,
        "Kampala": 24,
    }
    
    key = f"{city.strip().title()}|{date or 'today'}"
    rng = random.Random(key)
    city_t = city.strip().title()
    base = base_temps.get(city_t, 25)
    temp = base + rng.randint(-3, 3)
    condition = rng.choice(conditions)
    is_sunny = condition in {"Sunny", "Partly Cloudy"}

    return {
        "city": city_t,
        "date": date or "today",
        "condition": condition,
        "temperature_celsius": temp,
        "is_sunny": is_sunny
    }

def get_city_fact(city: str) -> Dict[str, str]:
    """
    Return a short, workshop-friendly fact for an African city.
    """
    facts = {
        "Nairobi": "Nairobi is the 'Green City in the Sun' and hosts Nairobi National Park.",
        "Lagos": "Lagos is one of Africa's largest cities and Nigeria's commercial hub.",
        "Cairo": "Cairo, on the Nile, is near the ancient Pyramids of Giza.",
        "Cape Town": "Cape Town is famous for Table Mountain and the Cape Winelands.",
        "Accra": "Accra is Ghana's coastal capital, known for its art and beaches.",
        "Kampala": "Kampala spans several hills near Lake Victoria, Uganda's cultural center.",
    }
    city_t = city.strip().title()
    return {"city": city_t, "fact": facts.get(city_t, f"{city_t} is a vibrant African city with rich culture.")}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="Answers questions with mock weather and city facts.",
    instruction=(
        "Use get_weather(city, date?) for weather. "
        "Use get_city_fact(city) for city facts. "
        "If the user asks for both (e.g., 'fact and weather'), call both tools and synthesize a single answer."
    ),
    tools=[get_weather, get_city_fact],
)
