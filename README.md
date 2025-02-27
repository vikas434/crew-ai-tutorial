# CrewAI Tutorial Series

This repository contains a comprehensive tutorial series on building AI applications using CrewAI. Each day focuses on different aspects of CrewAI, gradually building up to a complete travel planning system.

## Tutorial Structure

### Day 1: Basic Setup and Introduction
- Basic CrewAI concepts
- Simple agent creation
- Basic task execution
- OpenAI integration

### Day 2: Tools Integration
- Custom tool creation
- Tool integration with agents
- Basic error handling
- Utility functions

### Day 3: Enhanced Agents
- Multiple agent coordination
- Advanced task delegation
- Context sharing between agents
- Gemini AI integration

### Day 4: Complete Travel Planner
- Full-featured travel planning system
- Multiple tools and agents working together
- Advanced error handling
- Production-ready implementation

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (for Day 1)
- Gemini API key (for Days 3-4)

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

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

## Getting Started

Each day's tutorial is contained in its own directory with a complete README and example code:

1. Start with `day1/` to learn the basics
2. Move on to `day2/` to understand tool integration
3. Progress to `day3/` for advanced agent concepts
4. Finally, explore `day4/` for the complete travel planner

## Project Structure

```
crew-ai-tutorial/
├── day1/
│   ├── basic_setup/
│   │   ├── simple_openai.py
│   │   └── README.md
├── day2/
│   ├── tools_integration/
│   │   ├── tools.py
│   │   ├── basic_tools_demo.py
│   │   └── README.md
├── day3/
│   ├── enhanced_agents/
│   │   ├── multi_agent_demo.py
│   │   ├── simple_gemini.py
│   │   └── README.md
├── day4/
│   ├── travel_planner/
│   │   ├── enhanced_main.py
│   │   ├── tools.py
│   │   └── README.md
├── requirements.txt
└── .env.example
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
