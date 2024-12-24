import sys
import os
import yfinance as yf

def get_stock_prices():
    # Temporarily redirect stderr to suppress HTTP error messages
    stderr = sys.stderr  # Save the original stderr
    sys.stderr = open(os.devnull, 'w')  # Redirect errors to nowhere

    while True:
        stock_symbol = input("Enter the stock symbol (or 'stop' to exit): ").upper()
        
        if stock_symbol == 'STOP':
            break
            
        try:
            stock = yf.Ticker(stock_symbol)
            current_price = stock.info['currentPrice']
            print(f"${current_price:.2f}")
                            
        except:
            print(f"Error: Invalid symbol '{stock_symbol}'. Please enter a valid stock symbol.")

    # Restore stderr

    sys.stderr = stderr  # Restore original stderr

if __name__ == "__main__":
    get_stock_prices()

