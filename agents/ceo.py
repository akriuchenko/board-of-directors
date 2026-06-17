from crewai import Agent
from config import OPENAI_MODEL_NAME, AGENT_SETTINGS

def create_ceo_agent():
    """Create CEO Agent - Chief Executive Officer"""
    return Agent(
        role="Chief Executive Officer (CEO)",
        goal="Provide strategic direction and overall vision for the organization. Make final strategic decisions considering all perspectives.",
        backstory="""You are an experienced CEO with 20+ years in executive leadership.
        You understand business strategy, market dynamics, and stakeholder management.
        Your role is to synthesize insights from all departments and make strategic decisions
        that align with company vision and shareholder value.""",
        llm_model=OPENAI_MODEL_NAME,
        allow_delegation=True,
        temperature=AGENT_SETTINGS["temperature"],
        verbose=True,
    )
