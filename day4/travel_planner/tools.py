"""
Custom tools for the CrewAI travel planning system.

This module provides a set of tools that can be used by CrewAI agents to gather information
and perform calculations. Each tool is implemented as a function and wrapped using
langchain's Tool class for integration with CrewAI.

Tools:
    - current_date_tool: Get the current date and time
    - weather_tool: Get weather information for a location (mock implementation)
    - calculator_tool: Perform basic arithmetic operations
"""

from langchain.tools import Tool
import datetime
from typing import Union, Tuple

def get_current_date() -> str:
    """
    Get the current date and time in a formatted string.

    Returns:
        str: Current date and time in YYYY-MM-DD HH:MM:SS format
    """
    return f"Current date and time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def get_weather(location: str) -> str:
    """
    Get the current weather for a given location.
    Note: This is a mock implementation. In a production environment,
    this should be connected to a real weather API.

    Args:
        location (str): Name of the location to get weather for

    Returns:
        str: Mock weather information for the location

    Raises:
        ValueError: If location is empty or not a string
    """
    if not location or not isinstance(location, str):
        raise ValueError("Location must be a non-empty string")
    
    # Mock implementation
    return f"The weather in {location} is currently sunny and 72 degrees Fahrenheit."

def simple_calculator(operation: str, a: float, b: float) -> str:
    """
    Perform basic arithmetic calculations.

    Args:
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'
        a (float): First number
        b (float): Second number

    Returns:
        str: Result of the calculation in a formatted string

    Raises:
        ValueError: If operation is not supported or numbers are invalid
        ZeroDivisionError: If attempting to divide by zero
    """
    # Validate inputs
    if not operation or not isinstance(operation, str):
        raise ValueError("Operation must be a non-empty string")
    
    try:
        a = float(a)
        b = float(b)
    except (TypeError, ValueError):
        raise ValueError("Both numbers must be valid numeric values")

    # Perform calculation
    operation = operation.lower()
    if operation == "add":
        return f"{a} + {b} = {a + b}"
    elif operation == "subtract":
        return f"{a} - {b} = {a - b}"
    elif operation == "multiply":
        return f"{a} * {b} = {a * b}"
    elif operation == "divide":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return f"{a} / {b} = {a / b}"
    else:
        raise ValueError(f"Unknown operation: {operation}. Supported operations are: add, subtract, multiply, divide")

# Create tools using langchain's Tool class
current_date_tool = Tool(
    name="current_date",
    description="Get the current date and time",
    func=get_current_date
)

weather_tool = Tool(
    name="get_weather",
    description="Get the current weather in a given location. Input should be a city name.",
    func=get_weather
)

calculator_tool = Tool(
    name="simple_calculator",
    description="""Perform simple calculations. Operations supported: add, subtract, multiply, divide. 
    Input should be operation name followed by two numbers.""",
    func=simple_calculator
) 