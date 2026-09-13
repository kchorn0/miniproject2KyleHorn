# INF601 - Advanced Programming in Python
# Kyle Horn
# Mini Project 2

import os
import numpy as np 
import matplotlib.pyplot as plt
import yfinance as yf

# 5 favorite stock tickers to pull data for
TICKERS = ["AAPL", "MSFT", "AMZN", "GOOGL", "NVDA"]

# Data source used for this project (documented per assignment requirements)
DATA_SOURCE = "yfinance"

# Name of the folder where chart PNG files will be saved
CHARTS_DIR = "charts"


# Function that gets one ticker's last 10 trading days of closing prices.
# This covers the "collect closing price for last 10 trading days" requirement.
def get_last_10_closes(ticker):
    # Wrap the actual network calls to yfinance in a try/except, since a
    # bad ticker symbol, no internet connection, etc. could raise an error.
    try:
        # Create a yfinance Ticker object for this stock symbol.
        stock = yf.Ticker(ticker)

        # Start with 14 calendar days as a buffer against weekends/holidays.
        history = stock.history(period="14d")

        # If 14 days wasn't enough (extra holidays, data gaps, etc.),
        # try a wider window before giving up.
        if len(history) < 10:
            history = stock.history(period="1mo")
    except Exception as error:
        # Catches things like connection errors or an invalid ticker.
        print(f"Error fetching data for {ticker}: {error}")
        return None

    # Verify we actually received at least 10 trading days of data.
    try:
        # If we still don't have 10 rows even after the "1mo" fallback,
        # manually raise an error so it gets caught below.
        if len(history) < 10:
            raise ValueError(
                f"{ticker}: only got {len(history)} trading days, need at least 10"
            )
    except ValueError as error:
        print(f"Error fetching data for {ticker}: {error}")
        return None

    # Wrap the column lookup/conversion in case "Close" is ever missing.
    try:
        # Pull the "Close" column out and immediately turn it into a plain
        # Python LIST using the built-in list() function, as required.
        all_closes_list = list(history["Close"])
    except KeyError as error:
        print(f"Error reading closing prices for {ticker}: {error}")
        return None

    # Use normal Python list slicing to keep just the last 10 entries
    # (the most recent 10 trading days, oldest to newest).
    last_10_closes_list = all_closes_list[-10:]

    # Convert that LIST into a NumPy array, as required.
    closes_array = np.array(last_10_closes_list)

    # Return the NumPy array of closing prices.
    return closes_array


# Dictionary to hold every ticker's NumPy array of closing prices.
stock_data = {}

# Loop over all 5 tickers to fetch their data and fill in stock_data.
for symbol in TICKERS:
    # Get this ticker's last 10 closes back as a NumPy array.
    closing_prices = get_last_10_closes(symbol)

    # Save the NumPy array under its ticker symbol for later use.
    stock_data[symbol] = closing_prices

    # Print the ticker, the array itself, and confirm its type is NumPy.
    print(symbol, closing_prices, type(closing_prices))

# Wrapped in try/except in case of a permissions problem creating the folder.
try:
    # Create the charts folder if it doesn't already exist (exist_ok avoids
    # an error if it's already there). This covers the "create charts folder
    # if it doesn't exist" requirement.
    os.makedirs(CHARTS_DIR, exist_ok=True)
except OSError as error:
    # Report the problem but don't crash the whole program over it.
    print(f"Error creating charts folder: {error}")

# Now plot a graph for each ticker using Matplotlib.
for symbol in TICKERS:
    # Look up this ticker's NumPy array of closing prices.
    closing_prices = stock_data[symbol]

    # Skip this ticker entirely if we never got usable data for it.
    if closing_prices is None:
        print(f"Skipping plot for {symbol}: no data available")
        continue

    # "If" statement to verify we have at least the required 10 data points
    # before we bother plotting this ticker.
    if closing_prices.size < 10:
        print(f"Skipping plot for {symbol}: only {closing_prices.size} data points")
        continue

    # Build x-axis values: 0-9, one for each of the 10 trading days.
    day_numbers = np.arange(closing_prices.size)

    # Create a new Figure and Axes for this ticker (object-oriented style).
    fig, ax = plt.subplots(figsize=(8, 4.5))

    # Plot the closing prices as a line with circular markers.
    ax.plot(day_numbers, closing_prices, marker="o", color="C0", linewidth=2)

    # Label the x-axis to show these are trading days.
    ax.set_xlabel("Trading Day (most recent 10)")

    # Label the y-axis to show these are closing prices in dollars.
    ax.set_ylabel("Closing Price (USD)")

    # Title the chart with the ticker symbol so it's clear which stock it is.
    ax.set_title(f"{symbol} - Last 10 Trading Days Closing Price")

    # Turn on a light grid to make the chart easier to read.
    ax.grid(True, alpha=0.3)

    # Build the full file path for this ticker's PNG inside the charts folder.
    chart_path = os.path.join(CHARTS_DIR, f"{symbol}.png")

    # Wrap the file save in try/except in case of a permissions problem.
    try:
        # Save the figure as a PNG file instead of just displaying it.
        # This covers the "save graphs as PNG files" requirement.
        fig.savefig(chart_path)

        # Let the user know where this chart was saved.
        print(f"Saved chart for {symbol} to {chart_path}")
    except OSError as error:
        # Report the problem but don't crash the whole program over it.
        print(f"Error saving chart for {symbol}: {error}")

    # Close the figure to free up memory now that it's saved.
    plt.close(fig)
