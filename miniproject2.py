# INF601 - Advanced Programming in Python
# Kyle Horn
# Mini Project 2

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# 5 favorite stock tickers to pull data for
TICKERS = ["AAPL", "MSFT", "AMZN", "GOOGL", "NVDA"]

# Data source used for this project (documented per assignment requirements)
DATA_SOURCE = "yfinance"


def get_last_10_closes(ticker):
    """
    Get the closing price for the last 10 TRADING days for one ticker.

    We can't just ask for "10 days" of history, because weekends and
    market holidays (e.g. Labor Day on a Monday) mean 10 calendar days
    does not equal 10 trading days. Instead we request a larger window
    of calendar days (14, then fall back to 30 if needed), verify we
    actually got at least 10 rows of trading data back, and then trim
    down to just the most recent 10.
    """
    stock = yf.Ticker(ticker)

    # Start with 14 calendar days as a buffer against weekends/holidays.
    history = stock.history(period="14d")

    # If 14 days wasn't enough (extra holidays, data gaps, etc.),
    # try a wider window before giving up.
    if len(history) < 10:
        history = stock.history(period="1mo")

    # Verify we actually received at least 10 trading days of data.
    try:
        if len(history) < 10:
            raise ValueError(
                f"{ticker}: only got {len(history)} trading days, need at least 10"
            )
    except ValueError as error:
        print(f"Error fetching data for {ticker}: {error}")
        return None

    # Trim down to just the most recent 10 trading days, oldest to newest.
    last_10_days = history.tail(10)

    # Pull out just the closing prices.
    closes = last_10_days["Close"]

    return closes


# Quick check that data retrieval works before moving on to NumPy/Matplotlib.
for symbol in TICKERS:
    closing_prices = get_last_10_closes(symbol)
    print(symbol, closing_prices)
