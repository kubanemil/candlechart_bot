from tools import get_data, create_plot

# fn = input('')
df = get_data('prices.csv')

candlestick_interval = '12H'
# display_interval = (datetime.date())

candle_data = df.resample(candlestick_interval).apply({
    "price": ["first", "max", "min", "last"]
})

candle_data.columns = ["open", "high", "low", "close"]
ema_period = 2
max_period = len(candle_data)
if ema_period > max_period:
    raise ValueError(f'Period is more than allowed! Your period: {ema_period} (Max period: {max_period})')

create_plot(candle_data)