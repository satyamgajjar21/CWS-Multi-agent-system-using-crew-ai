# CWS Multi Agent System using CrewAI

A multi agent AI application built with CrewAI that performs live stock market analysis and generates trading recommendations using collaborative AI agents.

The system demonstrates how multiple autonomous agents can work together by sharing information, completing specialized tasks, and producing a final decision based on real-time market data.

---

## Features

- Multi Agent Architecture using CrewAI
- Live stock market data from Yahoo Finance
- Financial Market Analyst Agent
- Strategic Stock Trader Agent
- Interactive web interface
- Real-time execution timeline
- Modular agent and task design
- Powered by Groq Llama 3.3 70B

---

## Architecture

```text
                    User
                      │
                      ▼
              Web Frontend (HTML)
                      │
                      ▼
             Python HTTP Server
                      │
                      ▼
              CrewAI Orchestrator
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
Financial Market Analyst      Strategic Stock Trader
        │                           ▲
        │                           │
        ▼                           │
 Live Stock Information Tool ───────┘
        │
        ▼
 Yahoo Finance API

                ▼
      Final Buy / Sell / Hold Decision
```

---

## Workflow

```text
User enters stock symbol
            │
            ▼
Financial Analyst Agent
            │
            ▼
Calls Live Stock Tool
            │
            ▼
Retrieves live market data
            │
            ▼
Creates stock analysis
            │
            ▼
Strategic Trader Agent
            │
            ▼
Evaluates analysis
            │
            ▼
Returns

Buy
Sell
or
Hold
```

---

## Project Structure

```text
CWS-Multi-agent-system-using-crew-ai
│
├── agents
│   ├── analyst_agent.py
│   └── trader_agent.py
│
├── tasks
│   ├── analyse_task.py
│   └── trade_task.py
│
├── tools
│   └── stock_research_tool.py
│
├── crew.py
├── main.py
├── app.py
├── llm_config.py
├── index.html
├── requirements.txt
└── README.md
```

---

## Agents

### Financial Market Analyst

Responsibilities

- Retrieve live stock information
- Analyze current market performance
- Evaluate price movement
- Review market activity
- Generate structured analysis

Uses

- Live Stock Information Tool

Output

- Current price
- Daily change
- Volume
- Market observations

---

### Strategic Stock Trader

Responsibilities

- Review analyst report
- Evaluate trading opportunity
- Assess momentum
- Recommend action

Output

- Buy
- Sell
- Hold

along with reasoning.

---

## Tasks

### Task 1

Stock Analysis

The analyst gathers live market information including

- Current price
- Daily movement
- Percentage change
- Volume
- Market observations

---

### Task 2

Trading Decision

The trader evaluates the analysis and recommends

- Buy
- Sell
- Hold

with supporting reasoning.

---

## Tool

### Live Stock Information Tool

Uses

- Yahoo Finance

Returns

- Current stock price
- Daily change
- Percentage change
- Currency

---

## Tech Stack

| Component | Technology |
|------------|------------|
| Multi Agent Framework | CrewAI |
| LLM | Groq Llama 3.3 70B |
| Language | Python |
| Stock Data | Yahoo Finance |
| Frontend | HTML CSS JavaScript |
| Backend | Python HTTP Server |

---

<img width="1235" height="825" alt="image" src="https://github.com/user-attachments/assets/a4e96fa8-7074-4bc5-b453-71e19d425c57" />

<img width="1235" height="825" alt="Screenshot 2026-07-05 at 11 30 49 AM" src="https://github.com/user-attachments/assets/6da3b53b-44ce-4787-91e8-34bf3d6bee48" />



## Installation

Clone the repository

```bash
git clone https://github.com/satyamgajjar21/CWS-Multi-agent-system-using-crew-ai.git

cd CWS-Multi-agent-system-using-crew-ai
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env`

```text
GROQ_API_KEY=your_api_key
```

---

## Run

```bash
python app.py
```

Open

```
http://127.0.0.1:8000
```

---

## Example

Input

```
AAPL
```

Execution

```
Financial Market Analyst
        │
        ▼
Live Stock Tool
        │
        ▼
Stock Analysis
        │
        ▼
Strategic Stock Trader
        │
        ▼
Buy / Sell / Hold
```

---

## Future Improvements

- Multiple financial tools
- News sentiment analysis
- SEC filing analysis
- Historical trend analysis
- Portfolio management
- Risk scoring
- Memory-enabled agents
- Multi-agent collaboration with hierarchical process
- Streaming responses
- Authentication
- REST API

## Dependencies

- CrewAI
- CrewAI Tools
- yfinance
- python-dotenv

---

## Learning Objectives

This project demonstrates

- CrewAI multi-agent architecture
- Agent collaboration
- Task orchestration
- Tool calling
- LLM integration
- Live API integration
- Modular AI application design
- Interactive frontend with AI backend

---

## License

MIT License

---

## Author

**Satyam Gajjar**

GitHub

https://github.com/satyamgajjar21

LinkedIn


https://www.linkedin.com/in/Satyam

Website

https://www.satyamgajjar.com
