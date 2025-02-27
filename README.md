# CrewAI Travel Planning System

This project demonstrates an advanced implementation of CrewAI for automated travel planning. It uses multiple AI agents working together to research and create personalized travel itineraries.

## Features

- Research Analyst agent that gathers travel information
- Travel Advisor agent that creates personalized recommendations
- Custom tools for:
  - Weather information
  - Date/time operations
  - Budget calculations

## Prerequisites

- Python 3.8 or higher
- Gemini API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd crew-ai-tutorial
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

Run the enhanced travel planning system:
```bash
python enhanced_main.py
```

The system will:
1. Research travel conditions for New York City
2. Calculate budget information
3. Generate a detailed 3-day travel itinerary

## Project Structure

- `enhanced_main.py`: Main script that orchestrates the AI agents
- `tools.py`: Custom tools used by the agents
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (not tracked in git)

## Error Handling

The system includes robust error handling for:
- Missing API keys
- Invalid tool inputs
- Runtime exceptions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
