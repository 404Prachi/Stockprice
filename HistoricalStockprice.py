# Import yfinance and matplotlib
import yfinance as yf
import matplotlib.pyplot as plt
# Get the data for the SPY ETF by specifying the stock ticker, start date, and end date
data = yf.download('SPY', '2022-01-25', '2022-02-03')
print(data)
data["Adj Close"].plot()
plt.show()
print(data)
