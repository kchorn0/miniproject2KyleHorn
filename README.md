# miniproject2KyleHorn

## What this project does

This project pulls real stock market data for 5 tickers (AAPL, MSFT, AMZN,
GOOGL, NVDA), gets the closing price for each of the last 10 **trading**
days, stores that data in NumPy arrays, and plots each ticker as a line
chart with Matplotlib. Each chart is saved as a PNG file in the `charts/`
folder.

Data source used: **yfinance**.

## Requirements

- Python 3
- A virtual environment (recommended)

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
Be sure terminal says (.venv)

## How to run

```bash
python miniproject2.py
```

This will:
1. Fetch the last 10 trading days of closing prices for each ticker.
2. Store the data in NumPy arrays.
3. Create the `charts/` folder if it doesn't already exist.
4. Save a PNG chart for each ticker into `charts/`.

The `charts/` folder is tracked in this repo, but the generated PNG files
are not (see `.gitignore`) — they're created fresh each time you run the
program.

## AI Usage

Claude (Claude Code) was used as a coding assistant throughout this
project to help write, explain, and incrementally build up
`miniproject2.py` one requirement at a time (headers/imports, fetching
trading-day data from yfinance with error handling, converting the data
to NumPy arrays, plotting with Matplotlib, saving PNGs to the `charts/`
folder, and writing this README). All code was reviewed and tested by me
before committing.
