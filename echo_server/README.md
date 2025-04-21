# FastMCP Echo Server

A simple echo server implementation using FastMCP framework.

## Description

This server provides a basic echo service that returns any text sent to it. It demonstrates the basic usage of the FastMCP framework for creating MCP tools.

## Requirements

- Python 3.x
- FastMCP library

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:

```bash
python echo_server/echo_server.py
```

2. The server provides one tool:
   - `echo`: Returns the input text exactly as provided

## Project Structure

```
.
├── echo_server/
│   └── echo_server.py    # Main server implementation
├── requirements.txt      # Project dependencies
└── README.md            # This file
```

## License

[Add your chosen license here]