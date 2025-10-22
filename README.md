# Emergency Vehicle Routing using Real-Time Network Communication 🚑

## Project Overview

This project simulates *emergency vehicle routing* with *real-time network communication* using Python.  
It demonstrates how a control center server communicates with an emergency vehicle client, calculates optimal routes using Dijkstra's algorithm, and updates the route dynamically in response to traffic congestion.  
The system ensures that emergency vehicles receive the *fastest possible route* in real-time, simulating the role of modern smart city traffic management.

---

## 🎯 SDG Alignment
This project supports *UN Sustainable Development Goal 11: Sustainable Cities and Communities*:

| SDG   | Goal                              | Alignment                                                                 |
|-------|----------------------------------|---------------------------------------------------------------------------|
| SDG 11 | Sustainable Cities and Communities | Improves urban emergency response efficiency and safety by dynamically calculating optimal routes and simulating traffic congestion management. |

## ⚙ Setup and Installation

### Prerequisites
- Python 3.x installed.
- Project folder contains server.py and client.py.

### Setup and Dependencies
1. Create and activate a virtual environment
python -m venv venv

On Windows
venv\Scripts\activate

On macOS/Linux
source venv/bin/activate

2. Install any dependencies (if needed)
pip install -r requirements.txt

Note: This project uses only Python standard libraries (socket, heapq, time)

---

## 💻 Usage

### Run the Server (Control Center)
python server.py 

### Run the Client (Emergency Vehicle)
python Client.py
