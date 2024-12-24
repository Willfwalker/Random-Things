# import yfinance as yf

# # Define the ticker symbol and the number of days
# ticker_symbol = "AAPL"
# num_days = 100

# # Create a loop to retrieve the data for each day
# # for i in range(num_days):
# #     # Calculate the period for the current day
# #     period = i = 1
    
# #     # Retrieve the data for the current day
# #     data = yf.Ticker(ticker_symbol).history(period='1d')["Close"].iloc[-period]
    
#     # Print the data for the current day
# data = yf.Ticker("TSLA").history(period="max", interval="1d")
# print(data["Close"])

import matplotlib.pyplot as plt 
import yfinance as yf

choosen_stock = "TSLA" #input("What Stock do you want ot get the current price of?: ")

num_day = '2y' #input("How far ago do you want to get the price of the stock?: '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'].").lower()
ticker = yf.Ticker(choosen_stock)

# if num_days == "1d" or num_days == "2d" or num_days == "3d":
#     data = yf.Ticker("TSLA").history(period=num_days, interval="1h")
#     data['Close'].plot()

# if num_days == "5d" or num_days == "10d" or num_days == "1mo":
#     data = yf.Ticker("TSLA").history(period=num_days, interval="1d")
#     data['Close'].plot()

# else:
#     data = yf.Ticker("TSLA").history(period=num_days, interval="10d")
#     data['Close'].plot()



data = yf.Ticker("TSLA").history(period="max", interval="1d")
data['Close'].plot()

plt.plot(data['Close'])
plt.show()



