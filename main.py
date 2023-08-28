from tools import get_data, get_ema, convert_to_ohlc, create_plot

if input('Customize the parameters?(Y/n) ').lower() == 'y':
    # Inputs
    fn = input('1. Enter a data\'s file name.\n(Press "ENTER" for default="prices.csv"): ')

    print('\n2. Enter an interval for candlestick (ex. 2 days => 2D or 10 hours = > 10H or 15 mintues => 15T')
    candlestick_interval = input('(Press "ENTER" for (default="12H")): ') or '12H'

    ema_period = int(input(f'\n3. Enter a period to calculate EMA.\n(Press "ENTER" for default="12H"): ') or 3)

    print('\n4. Enter which period to display in percents (e.g. 10-65 will show a date from 10% to 65%')
    display_period = (input('(Press "ENTER" to show for entire period): ') or '0-100').split('-')

else:
    fn, candlestick_interval, ema_period, display_period = 'prices.csv', '12H', 3, (0, 100)


df = get_data('prices.csv', start=int(display_period[0]), end=int(display_period[1]))
candle_data = convert_to_ohlc(df, interval=candlestick_interval)
ema = get_ema(candle_data, period=ema_period)
# Final Plot
plot, ax = create_plot(candle_data, ema=ema)
plot.show()