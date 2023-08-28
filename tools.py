import mplfinance as mpf
import pandas as pd


def get_data(fn='prices.csv', start=0, end=100):
    df = pd.read_csv('prices.csv')
    df_len = len(df)
    df = df[int(df_len*start/100): int(df_len*end/100)]
    df["TS"] = pd.to_datetime(df["TS"])
    df.columns = ['timestamp', 'price']
    df.set_index("timestamp", inplace=True)
    return df


def convert_to_ohlc(df, interval='1D'):
    candle_data = df.resample(interval).apply({
        "price": ["first", "max", "min", "last"]
    })

    candle_data.columns = ["open", "high", "low", "close"]
    return candle_data


def get_ema(data, period):
    ema = data['close'].ewm(span=period, adjust=False).mean()
    return ema


def create_plot(data, ema):
    return mpf.plot(data, type='candle', style='charles', title="Candlestick Chart with EMA",
             addplot=[mpf.make_addplot(ema, color='orange')], ylabel='Price', xlabel='Date',
             figratio=(15, 6), returnfig=True)