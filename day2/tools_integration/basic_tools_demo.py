"""
Basic Tools Demo

This script demonstrates the usage of custom tools with CrewAI agents.
It shows how to create and use tools for date operations, weather information,
and basic calculations.
"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from tools import current_date_tool, weather_tool, calculator_tool

# Load environment variables
load_dotenv()

# Create an agent with tools
research_agent = Agent(
    role="Research Assistant",
    goal="Demonstrate the usage of various tools",
    backstory="""You are a helpful assistant demonstrating how to use different tools.
    You'll show how to get current date, weather information, and perform calculations.""",
    verbose=True,
    allow_delegation=False,
    tools=[current_date_tool, weather_tool, calculator_tool]
)

# Create a demonstration task
demo_task = Task(
    description="""Demonstrate the usage of all available tools by:
    1. Getting the current date
    2. Checking the weather in New York
    3. Calculating the sum of 150 and 250
    4. Calculating 1000 divided by 4
    Provide a summary of all results.""",
    agent=research_agent,
    expected_output="A demonstration of all tool functionalities with results"
)

# Create the crew
demo_crew = Crew(
    agents=[research_agent],
    tasks=[demo_task],
    verbose=True
)

# Run the demonstration
if __name__ == "__main__":
    result = demo_crew.kickoff()
    print("\n\n========================")
    print("Tool Demonstration Results:")
    print("========================\n")
    print(result) 