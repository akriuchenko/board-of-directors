#!/usr/bin/env python3
"""Board of Directors - CrewAI Multi-Agent System

This is the main entry point for the Board of Directors system.
It orchestrates a meeting between multiple specialized agents representing
different corporate roles to make strategic decisions.
"""

import os
from crewai import Crew
from dotenv import load_dotenv

from agents import (
    create_ceo_agent,
    create_cfo_agent,
    create_coo_agent,
    create_cqo_agent,
    create_supply_chain_agent,
    create_engineering_agent,
    create_devils_advocate_agent,
    create_production_agent,
    create_rd_director_agent,
    create_military_user_agent,
    create_auditor_agent,
)
from tasks import create_all_tasks
from utils import format_output, log_message


load_dotenv()


def initialize_board():
    """Initialize all board members (agents)"""
    log_message("Initializing Board of Directors...")
    
    agents = [
        create_ceo_agent(),
        create_cfo_agent(),
        create_coo_agent(),
        create_cqo_agent(),
        create_supply_chain_agent(),
        create_engineering_agent(),
        create_devils_advocate_agent(),
        create_production_agent(),
        create_rd_director_agent(),
        create_military_user_agent(),
        create_auditor_agent(),
    ]
    
    log_message(f"Board initialized with {len(agents)} agents", "INFO")
    return agents


def conduct_board_meeting(topic: str):
    """Conduct a board meeting on the given topic"""
    
    print(format_output("Board of Directors Meeting", f"Topic: {topic}"))
    log_message(f"Starting board meeting on: {topic}")
    
    # Initialize agents
    agents = initialize_board()
    
    # Create tasks
    tasks = create_all_tasks(topic)
    
    # Create and execute crew
    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True,
        process="sequential"  # Execute tasks sequentially
    )
    
    log_message("Executing board discussion...")
    result = crew.kickoff()
    
    print(format_output("Board Meeting Results", str(result)))
    log_message("Board meeting completed", "INFO")
    
    return result


def main():
    """Main function"""
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set")
        print("Please set your OpenAI API key before running this application")
        return
    
    # Example topics for board discussion
    topics = [
        "Develop a strategy for expanding into the Asian market with a focus on manufacturing optimization and military applications",
        "Evaluate the feasibility of developing a new line of AI-powered products for enterprise customers",
        "Assess the risks and opportunities of a major acquisition in the defense technology sector",
    ]
    
    # Conduct board meeting
    print("\n" + "="*80)
    print("Welcome to the Board of Directors Meeting")
    print("="*80 + "\n")
    
    # Use the first topic or accept user input
    topic = topics[0]
    print(f"Discussion Topic: {topic}\n")
    
    # Uncomment to use user input instead:
    # topic = input("Enter the topic for board discussion: ")
    
    result = conduct_board_meeting(topic)
    
    print("\n" + "="*80)
    print("Board meeting concluded")
    print("="*80)


if __name__ == "__main__":
    main()
