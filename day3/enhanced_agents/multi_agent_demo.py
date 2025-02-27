"""
Multi-Agent Demo

This script demonstrates how multiple agents can work together using CrewAI.
It shows agent coordination, task delegation, and information sharing between agents.
"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
import sys
sys.path.append('../../day2/tools_integration')
from tools import current_date_tool, weather_tool, calculator_tool

# Load environment variables
load_dotenv()

# Set up Gemini
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

def create_agents():
    """Create the specialized agents."""
    
    # Research Agent
    researcher = Agent(
        role="Research Analyst",
        goal="Gather and analyze information about technology trends",
        backstory="""You are an expert research analyst specializing in technology trends.
        You excel at gathering and analyzing information from various sources.""",
        verbose=True,
        allow_delegation=True,
        llm="gemini/gemini-1.5-flash",
        tools=[current_date_tool, weather_tool]
    )

    # Writer Agent
    writer = Agent(
        role="Technical Writer",
        goal="Create engaging content based on research",
        backstory="""You are a skilled technical writer who can transform complex
        information into engaging and accessible content.""",
        verbose=True,
        allow_delegation=True,
        llm="gemini/gemini-1.5-flash"
    )

    # Data Analyst Agent
    analyst = Agent(
        role="Data Analyst",
        goal="Analyze numerical data and provide insights",
        backstory="""You are a data analyst who excels at numerical analysis
        and providing actionable insights from data.""",
        verbose=True,
        allow_delegation=True,
        llm="gemini/gemini-1.5-flash",
        tools=[calculator_tool]
    )

    return [researcher, writer, analyst]

def create_tasks(agents):
    """Create tasks for the agents."""
    
    # Research Task
    research_task = Task(
        description="""Research the current state of AI technology:
        1. Get the current date for timeline reference
        2. Identify 3 major AI trends
        3. Gather specific examples of AI applications""",
        agent=agents[0],  # Researcher
        expected_output="A comprehensive research report on AI trends"
    )

    # Analysis Task
    analysis_task = Task(
        description="""Analyze the growth metrics for AI adoption:
        1. Calculate the year-over-year growth (use 25% and 100% as example numbers)
        2. Project the growth for next year
        3. Provide numerical insights""",
        agent=agents[2],  # Analyst
        expected_output="A detailed analysis of AI growth metrics",
        context=[research_task]
    )

    # Writing Task
    writing_task = Task(
        description="""Create an engaging blog post that combines the research and analysis:
        1. Use the research findings
        2. Incorporate the numerical analysis
        3. Make it engaging for a general audience
        4. Keep it under 600 words""",
        agent=agents[1],  # Writer
        expected_output="An engaging blog post about AI trends and growth",
        context=[research_task, analysis_task]
    )

    return [research_task, analysis_task, writing_task]

def main():
    """Run the multi-agent demonstration."""
    try:
        # Create agents and tasks
        agents = create_agents()
        tasks = create_tasks(agents)

        # Create the crew
        crew = Crew(
            agents=agents,
            tasks=tasks,
            verbose=True,
            process=Process.sequential
        )

        # Execute the tasks
        result = crew.kickoff()

        # Print the results
        print("\n\n========================")
        print("Final Blog Post:")
        print("========================\n")
        print(result)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 