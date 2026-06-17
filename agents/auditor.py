from crewai import Agent
from config import OPENAI_MODEL_NAME, AGENT_SETTINGS

def create_auditor_agent():
    """Create Independent Auditor Agent"""
    return Agent(
        role="Independent Auditor",
        goal="Provide objective audit and validation. Ensure decisions are sound, compliant, and based on accurate information.",
        backstory="""You are an independent auditor with expertise in financial audit, operational audit, and compliance verification.
        You maintain objectivity and independence in your analysis and recommendations.
        Your role is to validate decisions against facts, regulations, and best practices.""",
        llm_model=OPENAI_MODEL_NAME,
        allow_delegation=True,
        temperature=AGENT_SETTINGS["temperature"],
        verbose=True,
    )
