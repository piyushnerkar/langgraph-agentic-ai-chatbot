# LangGraph Agentic AI Chatbot

A modular agentic AI chatbot built with **LangGraph**, **Groq**, **Tavily**, and **Streamlit**. The application supports both a basic conversational workflow and a web-enabled agent that can use Tavily to retrieve current information from the web.

## Features

- Modular LangGraph architecture
- Stateful graph-based workflow
- Groq LLM integration
- Current Groq GPT-OSS models
- Tavily web search integration
- LangGraph `ToolNode`
- Conditional tool routing using `tools_condition`
- Streamlit user interface
- Configurable LLM and use-case selection
- Secure API-key input through the UI
- Dependency management with `uv`

## Architecture

```text
                         User
                           |
                           v
                    Streamlit UI
                           |
                           v
                    LangGraph Graph
                           |
                           v
                       Chatbot
                           |
                    tools_condition
                      /         \
                     /           \
              Tool required?      No
                   |               |
                   v               v
             Tavily Search       END
                   |
                   v
             Search Results
                   |
                   v
                Chatbot
                   |
                   v
             Final Response
```

## Project Structure

```text
langgraph-agentic-ai-chatbot/
|
├── app.py
├── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
|
└── src/
    └── langgraphagenticai/
        |
        ├── LLM/
        │   └── groqllm.py
        |
        ├── graph/
        │   └── graph_builder.py
        |
        ├── nodes/
        │   ├── basic_chatbot_node.py
        │   └── chatbot_with_Tool_node.py
        |
        ├── state/
        │   └── state.py
        |
        ├── tools/
        │   └── search_tool.py
        |
        └── ui/
            ├── uiconfig.ini
            └── streamlitui/
                ├── displayresult.py
                ├── loadui.py
                └── uiconfigfile.py
```

## How It Works

### Basic Chatbot

The basic workflow uses a LangGraph state containing the conversation messages.

```text
User
 ↓
Chatbot Node
 ↓
Groq LLM
 ↓
Response
```

### Chatbot With Web

When the web-enabled use case is selected, the Groq model is provided with the Tavily search tool.

The LLM can decide when external information is required.

```text
User Query
    ↓
Chatbot Node
    ↓
Tool Decision
    ↓
Tavily Search
    ↓
Search Results
    ↓
Chatbot Node
    ↓
Final Answer
```

The tool workflow is implemented using LangGraph's `ToolNode` and conditional routing.

## Technologies

- Python
- LangGraph
- LangChain
- Groq
- Tavily
- Streamlit
- uv

## Installation

Clone the repository:

```bash
git clone https://github.com/piyushnerkar/langgraph-agentic-ai-chatbot.git
cd langgraph-agentic-ai-chatbot
```

Install dependencies using `uv`:

```bash
uv sync
```

## API Keys

The application requires:

- Groq API key
- Tavily API key when using the web-enabled chatbot

API keys should never be committed to GitHub.

The application accepts the keys through the Streamlit interface.

## Running the Application

Run:

```bash
uv run streamlit run app.py
```

Then open the Streamlit URL shown in the terminal.

Select:

```text
LLM: Groq
Usecase: Basic Chatbot
```

or:

```text
LLM: Groq
Usecase: Chatbot With Web
```

For the web-enabled workflow, provide a Tavily API key.

## Example

A query such as:

```text
Give me the latest updates on the Asian Games.
```

can trigger the Tavily web-search tool, retrieve current information, and provide the retrieved information to the LLM for generating the final response.

## Project Objective

The objective of this project is to demonstrate how to build a modular **tool-using agentic AI application with LangGraph**, including graph-based state management, LLM integration, external tool execution, conditional routing, and a Streamlit interface.