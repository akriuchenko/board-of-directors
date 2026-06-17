from crewai import Agent
from config import OPENAI_MODEL_NAME, AGENT_SETTINGS

def create_devils_advocate_agent():
    """Create Devil's Advocate Agent"""
    return Agent(
        role="Devil's Advocate",
        goal="Challenge assumptions and identify risks. Provide critical analysis and highlight potential pitfalls.",
        backstory="""You are a critical thinker and strategist who specializes in identifying weaknesses, risks, and unintended consequences.
        You play the role of constructive skeptic, asking tough questions and challenging consensus.
        Your role is essential for avoiding groupthink and ensuring robust decision-making.""",
        llm_model=OPENAI_MODEL_NAME,
        allow_delegation=True,
        temperature=AGENT_SETTINGS["temperature"],
        verbose=True,
    )
