# 🤖 Multi-Agent AI Assistant

A modular, intelligent assistant built using **LangChain**, powered by **OpenAI LLMs**, and equipped with real-world tools like web search, live weather, and Python code execution.

This project demonstrates **multi-agent orchestration**, where agents with specialized tools collaborate to reason, plan, and solve complex queries — just like humans.

---

## 🚀 Features

- 🔍 **Web Search Agent** using DuckDuckGo
- 🌦️ **Live Weather Agent** using WeatherStack API
- 🧠 **Python REPL Agent** for dynamic code execution
- 🤖 **AgentExecutor** for tool selection and task coordination
- 🖥️ **FastAPI** backend for LLM processing
- 🎨 **Streamlit** frontend for interactive user queries
- 🔄 **CI/CD Pipeline** using **GitHub Actions**
- 
---

## 🧠 How It Works

LangChain’s `AgentExecutor` enables a central LLM to:
1. Understand user queries
2. Select the appropriate tool(s) via function calls
3. Chain tool outputs and generate final answers

Each tool is independently defined and registered to support modularity and extensibility.

---

## 🛠️ Tech Stack

| Layer         | Tools & Frameworks                      |
|--------------|-----------------------------------------|
| LLM & Agent   | LangChain, OpenAI                       |
| Tools         | DuckDuckGo Search, Python REPL, Weather API |
| Backend       | FastAPI                                 |
| Frontend      | Streamlit                               |
| DevOps        | GitHub Actions, Docker-ready    |

---


