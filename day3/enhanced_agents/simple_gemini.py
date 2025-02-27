from dotenv import load_dotenv
import os
from crewai import Agent, Task, Crew, Process

# Load environment variables
load_dotenv()

# Set environment variables for Gemini
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Create an agent with direct model string
content_creator = Agent(
    role="Content Creator",
    goal="Create engaging blog content about technology",
    backstory="You are an experienced tech writer with a knack for making complex topics accessible.",
    verbose=True,
    allow_delegation=False,
    llm="gemini/gemini-1.5-flash"  # Using LiteLLM's format for Gemini
)

# Create a task
writing_task = Task(
    description="Write a short blog post about the impact of artificial intelligence on everyday life. Focus on practical examples. Keep it under 500 words.",
    expected_output="A concise, engaging blog post about AI in everyday life with practical examples.",
    agent=content_creator
)

# Create a crew with just the content creator
crew = Crew(
    agents=[content_creator],
    tasks=[writing_task],
    verbose=True,
    process=Process.sequential
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\nFinal Blog Post:")
    print(result) 