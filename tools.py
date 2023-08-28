import mplfinance as mpf
import pandas as pd


def get_data(fn='prices.csv'):
    df = pd.read_csv('prices.csv')
    df["TS"] = pd.to_datetime(df["TS"])
    df.columns = ['timestamp', 'price']
    df.set_index("timestamp", inplace=True)
    return df


def create_plot(data, ema_period=3):
    ema = data['close'].ewm(span=ema_period, adjust=False).mean()

    mpf.plot(data, type='candle', style='charles', title="Candlestick Chart with EMA",
             addplot=[mpf.make_addplot(ema, color='orange')], ylabel='Price')