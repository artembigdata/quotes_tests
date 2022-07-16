# Сначала импортируем модули pandas, requests, bs4:

import pandas as pd
import requests
import bs4
# Сохраним строку с адресом веб-страницы в переменную url:
url = 'https://www.macrotrends.net/stocks/charts/MCD/mcdonalds/net-income'
#Скачаем весь код веб-страницы:
source = requests.get(url).text

# Передадим полученный код функции BeautifulSoup:
soup = bs4.BeautifulSoup(source, 'lxml')
#Выберем одну таблицу с классом historical_data_table:
table = soup.select_one('.historical_data_table')

#Прочитаем эту таблицу с помощью pd.read_html:
pandas_table = pd.read_html(str(table))
pandas_table = pandas_table[0]

#Запишем датафрейм в CSV файл:

historical_data.to_csv('mcd_income.csv', # вылазит подчеркивание/ошибка. что делать?
                       index=False)
print(pandas_table)

