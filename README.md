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

## How to run (in terminal run)

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

## Help

Common problems and fixes:

- **`ModuleNotFoundError` for numpy/matplotlib/yfinance** — your virtual
  environment probably isn't activated, or the requirements haven't been
  installed yet. Make sure your terminal prompt shows `(.venv)`, then run
  `pip install -r requirements.txt` again.
- **No internet connection / yfinance returns no data** — yfinance needs
  a live connection to pull stock data. If a ticker fails, the program
  prints an error for that ticker and skips it instead of crashing.
- **Charts don't look updated** — the program overwrites the PNGs in
  `charts/` every time it runs, so just re-run it after making changes.

If you want to double check exactly which package versions are installed
in your virtual environment (useful for comparing against
`requirements.txt`), run:

```bash
pip list
```

## Authors

Contributors names and contact info

Kyle Horn (kchorn@mail.fhsu.edu)

## AI Usage

Before writing any code, I used NotebookLM to summarize the week's class
videos and notes, since I'm an online student and wasn't able to attend
class live. I then gave ChatGPT the project requirements from Blackboard
along with that NotebookLM summary and asked it to help me turn the
requirements into more specific, concrete tasks, such as where I'd need
`if` statements and `try`/`except` error handling.

With those revised requirements in hand, I started scaffolding
`miniproject2.py` myself, beginning with the header comments and imports.
From there, I had Claude Code incrementally build up the rest of the file
one requirement at a time: fetching the last 10 trading days of data from
yfinance with error handling, converting that data to NumPy arrays,
plotting it with Matplotlib, saving the charts as PNGs into the `charts/`
folder, and drafting this README. Claude Code and I reviewed and tested
each step together before committing it.

I created the overall structure/outline for the project myself, and I
personally ran and tested the code after every save to review the
results line by line. I also made sure I understood and added a comment
to every line of code Claude Code wrote, partly so I could explain it and
partly to double-check its work. A couple of things I changed: Claude
Code's first pass pulled in packages like pandas, scipy, and
BeautifulSoup that I either hadn't learned yet or wasn't actually using,
so I had those removed and trimmed `requirements.txt` down to just
numpy, matplotlib, and yfinance. I also asked for extra `try`/`except`
handling around creating the `charts/` folder and saving the PNG files,
which wasn't explicitly called for in the original requirements, because
I wanted to make sure this program wouldn't throw an unhandled traceback
in any reasonably likely situation.
