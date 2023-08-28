from tools import get_data, get_ema, convert_to_ohlc, create_plot

# Inputs
fn = input('1. Enter a data\'s file name ("ENTER" for default="prices.csv"): ')

print('\n2. Enter an interval for candlestick (ex. 2 days => 2D or 10 hours = > 10H or 15 mintues => 15T')
candlestick_interval = input('("ENTER" for (default="12H")): ') or '12H'

ema_period = int(input(f'\n3. Enter a period to calculate EMA (default_period=3): ') or 3)

print('\n4. Enter which period to display in percents (e.g. 10-65 will show a date from 10% to 65%')
display_period = (input('("ENTER" to show for all period): ') or '0-100').split('-')

df = get_data('prices.csv', start=int(display_period[0]), end=int(display_period[1]))
candle_data = convert_to_ohlc(df, interval=candlestick_interval)
ema = get_ema(candle_data, period=ema_period)
# Final Plot
create_plot(candle_data, ema=ema)
