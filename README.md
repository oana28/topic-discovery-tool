# TOPIC DISCOVERY TOOL

An AI research assistant that answers questions using web search and streams responses in real time.

## Tech stack

- Frontend: React, TypeScript

- Backend: FastAPI, Tavily (web search)

- AI Agent: LangChain, Ollama

- Containerization: Docker

## Getting started

### 1. Setup

Clone git repository

```bash
    git clone https://github.com/oana28/topic-discovery-tool.git
    cd backend
```

Create and activate virtual environment

```bash
    python -m venv venv
    venv\Scripts\activate
```

Install dependencies:

```bash
    pip install -r requirements.txt
```

### 2. Create '.env' file in the root directory

```bash
    TAVILY_API_KEY='...'
```

### 3. Start Ollama

```bash
    docker compose up ollama -d
```

### 4. Pull Ollama model

```bash
    docker compose exec ollama ollama pull qwen3
```

### 5. Start backend

```bash
    docker compose up --build
```

### 6. Verify backend

```
http://localhost:8000/docs
```

### 7. Open the app

```
http://localhost:5173/
```
