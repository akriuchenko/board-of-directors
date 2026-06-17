# Board of Directors - CrewAI Multi-Agent System

A sophisticated multi-agent system using CrewAI that simulates a corporate board of directors making strategic decisions collaboratively.

## Features

- **Multi-Agent Architecture**: 10 specialized agents representing different corporate roles
- **Strategic Decision-Making**: Agents collaborate to analyze and make decisions
- **Comprehensive Analysis**: Each agent brings their unique perspective and expertise
- **Task Orchestration**: Complex workflows with dependencies and sequential execution

## Agents

1. **CEO** - Chief Executive Officer: Strategic direction and overall vision
2. **CFO** - Chief Financial Officer: Financial analysis and fiscal responsibility
3. **COO** - Chief Operating Officer: Operations optimization and efficiency
4. **CQO** - Chief Quality Officer: Quality assurance and compliance
5. **Supply Chain Agent** - Supply chain optimization and logistics
6. **Engineering Agent** - Technical feasibility and innovation
7. **Devil's Advocate Agent** - Critical analysis and risk identification
8. **Production Head** - Manufacturing and production efficiency
9. **R&D Director** - Research and development strategy
10. **Military End User** - Defense/military sector requirements
11. **Independent Auditor** - Objective audit and validation

## Tasks

The system handles multiple task categories:

- Strategic Planning
- Decision Making
- Risk Assessment
- Quality Analysis
- Financial Planning
- Operational Optimization
- Supply Chain Optimization
- Production Strategy
- Research & Development Strategy
- Independent Validation

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Set your environment variables:

```bash
export OPENAI_API_KEY="your-api-key"
```

## Usage

```bash
python main.py
```

## Project Structure

```
board-of-directors/
├── main.py                 # Main entry point
├── config.py              # Configuration settings
├── agents/
│   ├── __init__.py
│   ├── ceo.py            # CEO Agent
│   ├── cfo.py            # CFO Agent
│   ├── coo.py            # COO Agent
│   ├── cqo.py            # CQO Agent
│   ├── supply_chain.py   # Supply Chain Agent
│   ├── engineering.py    # Engineering Agent
│   ├── devils_advocate.py# Devil's Advocate Agent
│   ├── production.py     # Production Head Agent
│   ├── rd_director.py    # R&D Director Agent
│   ├── military_user.py  # Military End User Agent
│   └── auditor.py        # Independent Auditor Agent
├── tasks/
│   ├── __init__.py
│   └── task_definitions.py # All task definitions
├── utils/
│   ├── __init__.py
│   └── helpers.py        # Utility functions
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables example
└── .gitignore           # Git ignore rules
```

## License

MIT License
