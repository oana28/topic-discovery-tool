# TOPIC DISCOVERY TOOL

An AI research assistant that answers questions using web search and streams responses in real time.

## Tech stack

**Backend**

- FastAPI
- Langchain
- Tavily
- Ollama + Qwen3

**Frontend**

- Vite
- React
- Typescript

## Prerequisites

- Docker
- Ollama
- API key for Tavily

## Getting started

### 1. Clone git repository

```bash
    git clone https://github.com/oana28/topic-discovery-tool.git
    cd backend
```

### 2. Add .env file which will contain the tavily api key

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

### 6. Verify backend running at `http://localhost:8000/docs`

### 7. Start frontend locally

```bash
    cd frontend
    npm install
    npm run dev
```

### 8. Open browser at `http://localhost:5173/`
