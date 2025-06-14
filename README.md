# LangGraph & LangChain Tools

This repository provides a minimal scaffolding for orchestrating LLM calls with LangGraph for control-flow and LangChain for reusable chains/tools.

## Structure

```
repo-root/
├── README.md
├── requirements.txt     # Core dependencies
├── pyproject.toml      # Black, Ruff, pytest config
├── tools/              # Main package
│   ├── __init__.py
│   ├── llm.py          # Abstract client + DummyLLM
│   └── graph.py        # build_simple_graph()
└── tests/
    └── test_graph.py   # Basic tests
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Graph Building

```python
from tools import build_simple_graph

# Build a simple graph with placeholder LLM
graph = build_simple_graph()
compiled_graph = graph.compile()

# This will raise NotImplementedError since we're using DummyLLM
try:
    result = compiled_graph.invoke({"prompt": "Hello, world!"})
except NotImplementedError as e:
    print(f"Expected: {e}")
```

### Swapping DummyLLM with Real Client

To use a real LLM client, implement the `LLMClient` interface:

```python
from tools.llm import LLMClient
from tools.graph import build_simple_graph

class MyLLMClient(LLMClient):
    def generate(self, prompt: str, **kwargs) -> str:
        # Your LLM implementation here (OpenAI, Ollama, etc.)
        return f"Response to: {prompt}"

# Use your custom LLM
my_llm = MyLLMClient()
graph = build_simple_graph(llm=my_llm)
compiled_graph = graph.compile()
result = compiled_graph.invoke({"prompt": "Hello, world!"})
print(result["response"])
```

## Development

### Testing

```bash
pytest
```

### Linting & Formatting

```bash
black --check .
ruff .
```

### Module Import Test

```bash
python -m tools.graph
```

## Requirements

- Python >= 3.10
- See `requirements.txt` for package dependencies