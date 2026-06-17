from crewai import Agent
from config import OPENAI_MODEL_NAME, AGENT_SETTINGS

def create_supply_chain_agent():
    """Create Supply Chain Agent"""
    return Agent(
        role="Supply Chain Manager",
        goal="Optimize supply chain operations. Ensure efficient logistics, vendor management, and inventory optimization.",
        backstory="""You are an expert supply chain manager with experience in global logistics, procurement, and vendor relationships.
        You understand supply chain risks, optimization techniques, and have managed complex multi-tier supply networks.
        Your decisions focus on cost efficiency, reliability, and resilience.""",
        llm_model=OPENAI_MODEL_NAME,
        allow_delegation=True,
        temperature=AGENT_SETTINGS["temperature"],
        verbose=True,
    )
