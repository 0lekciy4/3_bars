# Ближайшие бары

После запуска, программа у вас запросит ввести координаты через ", ".
Координаты вашего местоположения проще всего скопировать с яндекс карт,
нажав ПКМ по карте и выбрать "Что здесь?". После ввода координат
программа выведет на экаран информацию о самом ближайшем баре, самом
маленьком баре и самом большом баре. В информации о баре вы найдете
адресс, название и количество мест в баре.

# Как запустить

1. Скрипт требует для своей работы установленного интерпретатора Python
версии 3.5 .
2. Необходимо установить зависимости из requirements.txt
или установить geopy и requests.
3. Файл со списком баров необходимо скачть по ссылке https://data.mos.ru/opendata/7710881420-bary
разархивировать и указать путь к json файлу в качестве аргумента при зпуске программы,
если не указать путь то будет загружен список баров с https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json
```bash
pip3 install -r requirements.txt
```
или
```bash
pip3 install geopy
pip3 install requests
```


Запуск на Linux:

```bash

$ python bars.py <path_to_file>
Введите широту и долготу. Для примера:
55.754709, 37.618776
55.754709, 37.618776
========================================================================================================================
Ближайший бар - «ТД ГУМ бар в столовой» находится по адресу Красная площадь, дом 3 и там 10 мест
========================================================================================================================
Самый маленький бар - «БАР. СОКИ» находится по адресу Дубравная улица, дом 34/29 и там 0 мест
========================================================================================================================
Самый большой бар - «Спорт бар «Красная машина»» находится по адресу Автозаводская улица, дом 23, строение 1 и там 450 мест


```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
