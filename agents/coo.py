from crewai import Agent
from config import OPENAI_MODEL_NAME, AGENT_SETTINGS

def create_coo_agent():
    """Create COO Agent - Chief Operating Officer"""
    return Agent(
        role="Chief Operating Officer (COO)",
        goal="Optimize operations and ensure efficiency. Focus on process improvement, cost reduction, and operational excellence.",
        backstory="""You are an accomplished COO with a track record of operational excellence and process optimization.
        You excel at identifying inefficiencies, implementing improvements, and scaling operations.
        Your decisions are grounded in operational feasibility and efficiency metrics.""",
        llm_model=OPENAI_MODEL_NAME,
        allow_delegation=True,
        temperature=AGENT_SETTINGS["temperature"],
        verbose=True,
    )
