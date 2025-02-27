"""
Enhanced CrewAI Travel Planning System

This script demonstrates an advanced implementation of CrewAI for travel planning.
It creates a crew of AI agents that work together to research and plan travel itineraries.

The system uses:
- Research Analyst: Gathers travel information using various tools
- Travel Advisor: Creates personalized travel recommendations
- Custom tools: Weather, date, and calculator functionalities
"""

import os
import sys
from typing import Dict, List
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from tools import current_date_tool, weather_tool, calculator_tool

def load_environment() -> None:
    """
    Load environment variables and configure API keys.
    
    Raises:
        EnvironmentError: If required API keys are missing
    """
    load_dotenv()
    
    # Validate environment variables
    gemini_key = os.getenv("GEMINI_API_KEY")
    if not gemini_key:
        raise EnvironmentError("GEMINI_API_KEY not found in environment variables")
    
    # Set environment variables for Gemini
    os.environ["GOOGLE_API_KEY"] = gemini_key

def create_agents() -> List[Agent]:
    """
    Create and configure the AI agents for the travel planning system.
    
    Returns:
        List[Agent]: List of configured agents
    """
    # Create a research agent with tools
    researcher = Agent(
        role="Research Analyst",
        goal="Gather comprehensive information for a travel report",
        backstory="""You are a meticulous research analyst specializing in travel information.
        You use various tools to gather accurate and up-to-date information.""",
        verbose=True,
        allow_delegation=True,
        llm="gemini/gemini-1.5-flash",
        tools=[current_date_tool, weather_tool, calculator_tool]
    )

    # Create a travel advisor agent
    travel_advisor = Agent(
        role="Travel Advisor",
        goal="Create personalized travel recommendations",
        backstory="""You are an experienced travel advisor who creates tailored travel 
        recommendations based on research data. You consider weather conditions, 
        local events, and traveler preferences to create the perfect itinerary.""",
        verbose=True,
        allow_delegation=False,
        llm="gemini/gemini-1.5-flash"
    )

    return [researcher, travel_advisor]

def create_tasks(agents: List[Agent]) -> List[Task]:
    """
    Create tasks for the agents to execute.
    
    Args:
        agents (List[Agent]): List of available agents
        
    Returns:
        List[Task]: List of tasks to be executed
    """
    research_task = Task(
        description="""Research travel conditions for New York City. 
        Use the weather tool to check current conditions.
        Use the date tool to confirm the current date.
        Calculate the average daily budget for a 5-day trip with a total budget of $2000,
        accounting for $200 per night for accommodation.""",
        agent=agents[0],  # Research Analyst
        expected_output="A comprehensive travel research report for New York City"
    )

    advisory_task = Task(
        description="""Based on the research provided, create a detailed 3-day itinerary 
        for a trip to New York City. Include recommendations for activities, dining, and 
        transportation. Consider the weather conditions and budget constraints mentioned 
        in the research.""",
        agent=agents[1],  # Travel Advisor
        expected_output="A detailed 3-day New York City itinerary",
        context=[research_task]
    )

    return [research_task, advisory_task]

def main() -> None:
    """
    Main function to run the travel planning system.
    """
    try:
        # Load and validate environment
        load_environment()

        # Create agents and tasks
        agents = create_agents()
        tasks = create_tasks(agents)

        # Create and configure the crew
        travel_crew = Crew(
            agents=agents,
            tasks=tasks,
            verbose=True,
            process=Process.sequential
        )

        # Execute the crew's tasks
        result = travel_crew.kickoff()

        # Print the results
        print("\n\n========================")
        print("Final Travel Itinerary:")
        print("========================\n")
        print(result)

    except EnvironmentError as e:
        print(f"Environment Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 