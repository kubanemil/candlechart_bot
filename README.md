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
git install -r requirements.txt
```
7. Запускаем скрипт:
   ```shell
python3 main.py
```
После этого надо ввести все данные (Но можете нажимать "Enter" для запуска по умолчанию).

