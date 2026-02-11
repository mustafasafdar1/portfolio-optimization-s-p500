# data_loader.py

import yfinance as yf
import pandas as pd

def download_data(tickers, start_date, end_date):
    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        auto_adjust=True
    )


    if isinstance(data.columns, pd.MultiIndex):
        data = data["Close"]

    data.dropna(inplace=True)
    return data


def calculate_returns(data):
    return data.pct_change().dropna()
