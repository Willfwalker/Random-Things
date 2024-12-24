import yfinance as yf
import sys
import os
import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import Tim_Help

def plot_stock_data(symbol, days=30):
    try:
        stock = yf.Ticker(symbol)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Get historical data
        hist = stock.history(start=start_date, end=end_date)
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.plot(hist.index, hist['Close'])
        plt.title(f'{symbol} Stock Price - Last {days} Days')
        plt.xlabel('Date')
        plt.ylabel('Price ($)')
        plt.grid(True)
        plt.xticks(rotation=45)
        
        # Save the plot
        plt.savefig(f'{symbol}_stock_price.png', bbox_inches='tight')
        plt.close()
        
        print(f"Graph saved as {symbol}_stock_price.png")
    except Exception as e:
        print(f"Error creating graph for {symbol}: {str(e)}")

def get_stock_prices():
    # Temporarily redirect stderr to suppress HTTP error messages
    stderr = sys.stderr
    sys.stderr = open(os.devnull, 'w')

    # Create/open CSV file with headers
    with open('stock_prices.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write headers if file is empty
        if os.path.getsize('stock_prices.csv') == 0:
            writer.writerow(['Date', 'Symbol', 'Price'])

    while True:
        stock_symbol = input("Enter the stock symbol (or 'stop' to exit): ").upper()
        
        if stock_symbol == 'STOP':
            break
            
        try:
            stock = yf.Ticker(stock_symbol)
            current_price = stock.info['currentPrice']
            print(f"${current_price:.2f}")
            
            # Create graph
            plot_stock_data(stock_symbol)
            
            # Save to CSV
            with open('stock_prices.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                               stock_symbol, 
                               f"{current_price:.2f}"])
                
        except:
            print(f"Error: Invalid symbol '{stock_symbol}'. Please enter a valid stock symbol.")

    # Restore stderr
    sys.stderr = stderr

if __name__ == "__main__":
    get_stock_prices()

