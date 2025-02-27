# Day 1: Basic Setup and Introduction

This first tutorial introduces the basic concepts of CrewAI and demonstrates how to create a simple AI agent using OpenAI's GPT model.

## Concepts Covered

1. Basic CrewAI setup
2. Creating a single agent
3. Defining a simple task
4. Running the agent with OpenAI integration

## Files

- `simple_openai.py`: Basic example using a single agent with OpenAI

## Prerequisites

- OpenAI API key
- Python 3.8+
- Required packages from `requirements.txt`

## Setup

1. Ensure you have an OpenAI API key
2. Add your API key to `.env`:
```bash
OPENAI_API_KEY=your_key_here
```

## Running the Example

```bash
python simple_openai.py
```

This will create a content creator agent that writes a blog post about AI's impact on everyday life.

## Code Explanation

The example demonstrates:
- Loading environment variables
- Initializing the OpenAI model
- Creating an agent with a specific role and goal
- Defining a task for the agent
- Creating a crew with a single agent
- Executing the task and displaying results

## Expected Output

The script will generate a blog post about AI's impact on everyday life, demonstrating:
- Agent initialization
- Task execution
- Result formatting

## Next Steps

After completing this tutorial, proceed to Day 2 to learn about integrating custom tools with your agents. 