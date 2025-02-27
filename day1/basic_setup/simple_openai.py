import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import openai

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI model
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Create a single agent
content_creator = Agent(
    role="Content Creator",
    goal="Create engaging blog content about technology",
    backstory="""You are a skilled content creator with expertise in technology 
    and a talent for making complex topics accessible to general audiences.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Create a task for the agent
writing_task = Task(
    description="""Write a short, engaging blog post about the impact of artificial 
    intelligence on everyday life. Focus on 2-3 practical examples that readers 
    can relate to. Keep it under 500 words.""",
    agent=content_creator,
    expected_output="A concise, engaging blog post about AI in everyday life"
)

# Create the crew (with just one agent for simplicity)
content_crew = Crew(
    agents=[content_creator],
    tasks=[writing_task],
    verbose=True
)

# Run the crew
if __name__ == "__main__":
    result = content_crew.kickoff()
    print("\n\n========================")
    print("Final Blog Post:")
    print("========================\n")
    print(result) 