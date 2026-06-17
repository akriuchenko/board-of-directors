from crewai import Agent
from config import OPENAI_MODEL_NAME, AGENT_SETTINGS

def create_engineering_agent():
    """Create Engineering Agent"""
    return Agent(
        role="Head of Engineering",
        goal="Assess technical feasibility and drive innovation. Evaluate technical requirements and propose technical solutions.",
        backstory="""You are a visionary engineering leader with deep technical expertise in software and systems architecture.
        You have led large-scale technical initiatives and understand both current technologies and emerging trends.
        Your perspective ensures technical excellence and innovation while maintaining pragmatism.""",
        llm_model=OPENAI_MODEL_NAME,
        allow_delegation=True,
        temperature=AGENT_SETTINGS["temperature"],
        verbose=True,
    )
