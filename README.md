# Candlechart bot
Тех. задание

## Что делает
Эта программа строит Candlestick Chart и высчитывает EMA (Exponential Moving Average) из данных о волюте (или акциях). Данные должны быть в формате CSV и иметь
две колонны: timestamp и price

## Как установить
1. Клонируем репозиторий:
```shell
git clone https://github.com/kubanemil/candlechart_bot
```

3. Создаем виртуальную среду:
```shell
python3 -m venv venv
source venv/bin/activate
```

5. Устанваливаем сторонние библиотеки:
  ```shell
pip install -r requirements.txt
```

7. Запускаем скрипт:
```shell
python3 main.py
```

После этого надо ввести все данные (Но можете нажимать "Enter" для запуска по умолчанию).


## При запуске
При запуске кода, нужно ввести:
1. **Название csv-файла** с данными (должен содержать столбцы 'TS'(datetime) и 'PRICE'(int)). По умолчанию будет использовать файл 'prices.csv'.
2. **Интервал времени для candlestick**. Должен быть введен в следущем формате:
 - 10 часов => 10H
 - 2 дня => 2D
 - 45 минут => 45T
Например, если хотите чтобы интервал candlestick была взята за 2 часа, вы должны ввести 2H.
По умолчанию: 12H.
3. **Количество candlestickов** для рассчета **EMA**. Чем больше значение, тем плавнее будет **EMA**. По умолчанию: 3.
4. **Период времени** которое надо показать в **графике**. Указываем в процентном соотношении. Например, если укажите '10-35',
   то он покажет график за период от 10% до 35%. Полезно если вы хотите рассмотреть график детальнее за конкретный период времени.
   По умолчанию: 0-100 (покажет за все время). 
