import pandas_datareader as web
import datetime as dt
from datetime import datetime
import mplfinance as mpf

start = dt.datetime(datetime.now().year, datetime.now().month-2, 1)
end = dt.datetime.now()

# Altcoins also work
data = web.DataReader("DOGE-USD", "yahoo", start, end)

mpf.plot(data, type="candle", volume=True, mav=(3),  style="charles", title = "DOGE COIN Market Price")