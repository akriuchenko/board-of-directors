import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq Configuration (Free LLM API)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL_NAME = os.getenv("GROQ_MODEL_NAME", "mixtral-8x7b-32768")

# CrewAI Configuration
CREWAI_LOG_LEVEL = os.getenv("CREWAI_LOG_LEVEL", "INFO")

# Project Configuration
PROJECT_NAME = "Board of Directors"
PROJECT_DESCRIPTION = "Multi-Agent Strategic Decision Making System"

# Agent Configuration
AGENT_SETTINGS = {
    "temperature": 0.7,
    "max_tokens": 2000,
    "timeout": 300,
}

# Task Configuration
TASK_SETTINGS = {
    "enable_logging": True,
    "max_retries": 3,
}
