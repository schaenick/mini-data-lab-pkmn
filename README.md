# Pokémon Type Analyzer

This project explores Pokémon types and their statistical characteristics using a publicly available dataset.  
It aims to analyze type distribution, strengths and weaknesses between types and average stat performance through Python-based data analysis and visualization.

---

## Features

- Load Pokémon data from a CSV file  
- Analyze the number of Pokémon per type  
- Evaluate strengths and weaknesses between types  
- Calculate a score per type (tbd)  
- Create visualizations using Matplotlib  
- Modular project structure (loader, analysis, visualization)

---

## Project Structure
```text 
project/
│
├── data/
│   └── pokemon.csv
│
├── src/
│   ├── data_loader.py
│   ├── type_analysis.py
│   ├── stats_analysis.py
│   └── visualizations.py
│
└── README.md
```
---

## Installation

To run this project locally:

bash:
git clone https://github.com/schaenick/pokemon-analyzer
cd pokemon-analyzer

python -m venv .venv
.venv\Scripts\activate  

pip install -r requirements.txt

---
