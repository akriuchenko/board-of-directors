import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-4")

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
