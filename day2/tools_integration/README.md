# Day 2: Tools Integration

This tutorial focuses on creating and integrating custom tools with CrewAI agents. You'll learn how to create utility functions and wrap them as tools that agents can use.

## Concepts Covered

1. Creating custom tools
2. Tool integration with agents
3. Error handling in tools
4. Using multiple tools together

## Files

- `tools.py`: Custom tool definitions
- `basic_tools_demo.py`: Example script demonstrating tool usage

## Tools Implemented

1. Current Date Tool
   - Get current date and time
   - Basic datetime operations

2. Weather Tool
   - Get weather information (mock implementation)
   - Location-based data retrieval

3. Calculator Tool
   - Basic arithmetic operations
   - Error handling for invalid inputs

## Prerequisites

- Completion of Day 1
- Understanding of basic Python functions
- Knowledge of error handling

## Running the Example

```bash
python basic_tools_demo.py
```

This will demonstrate:
- Tool initialization
- Tool usage by agents
- Error handling
- Result formatting

## Code Explanation

The tutorial covers:
- Creating tool functions
- Adding proper documentation
- Implementing error handling
- Wrapping functions as CrewAI tools
- Using tools in agents

## Expected Output

The demo will show:
- Current date/time retrieval
- Weather information for a location
- Basic calculations
- Error handling in action

## Next Steps

After mastering tool integration, proceed to Day 3 to learn about enhanced agent capabilities and multi-agent coordination. 