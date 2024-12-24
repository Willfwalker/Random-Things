import matplotlib.pyplot as plt 
import yfinance as yf
import tkinter as tk
import os
from datetime import datetime, timedelta

# Define the save path
SAVE_PATH = "/Users/willwalker/Desktop/Coding/Random_Things/Tim Help Folder"

def plot_stock_data(symbol, period='30d'):
    """
    Plots and saves the stock closing prices for a given symbol and period.
    
    :param symbol: Stock ticker symbol (e.g., 'AAPL')
    :param period: Time period for the stock data (e.g., '1d', '5d', '1mo')
    """
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period)
        
        if hist.empty:
            print(f"No data found for symbol: {symbol} with period: {period}")
            return
        
        plt.figure(figsize=(10, 6))
        plt.plot(hist.index, hist['Close'], marker='o')
        plt.title(f'{symbol} Stock Price - Last {period}')
        plt.xlabel('Date')
        plt.ylabel('Price ($)')
        plt.grid(True)
        plt.xticks(rotation=45)
        
        # Ensure SAVE_PATH exists
        os.makedirs(SAVE_PATH, exist_ok=True)
        
        # Save to specified path
        save_file = os.path.join(SAVE_PATH, f'{symbol}_stock_price_{period}.png')
        plt.savefig(save_file, bbox_inches='tight')
        plt.close()
        
        print(f"Graph saved as {save_file}")
    except Exception as e:
        print(f"Error creating graph for {symbol}: {str(e)}")

def get_stock_prices():
    """
    Retrieves user input and plots the stock data.
    """
    symbol = choosen_stock.get().strip().upper()
    period = num_days.get().strip().lower()
    
    if not symbol:
        print("Please enter a stock symbol.")
        return
    if not period:
        print("Please enter the time period.")
        return
    
    plot_stock_data(symbol, period)
    window.destroy()

if __name__ == '__main__':
    window = tk.Tk()
    window.title("Stock Price")
    window.geometry("500x300")

    labelofwantedstocks = tk.Label(window, text="What stock do you want to get the current price of?")
    labelofwantedstocks.pack(pady=(20, 5))
    
    choosen_stock = tk.Entry(window, width=50)
    choosen_stock.pack(pady=(0, 10))

    labelofnumday = tk.Label(window, text="Select the time period for the stock price:")
    labelofnumday.pack(pady=(10, 5))
    
    labelofnumdays = tk.Label(window, text="[1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max]")
    labelofnumdays.pack(pady=(0, 10))
    
    num_days = tk.Entry(window, width=50)
    num_days.pack(pady=(0, 20))

    button = tk.Button(window, text="Graph", command=get_stock_prices)
    button.pack(pady=(0, 20))

    window.mainloop()

