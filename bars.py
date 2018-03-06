import json
import requests
import sys
from geopy.distance import great_circle


def download_data(site):
    geted_site = requests.get(site)
    site_data = geted_site.json()
    return site_data


def load_data(file_path):
    with open(file_path, 'r', encoding='UTF-8') as json_file:
        loaded_data = json.load(json_file)
    return loaded_data


def get_coordinates(bar):
    return bar['geometry']['coordinates']


def get_closest_bar(bars, my_coord):
    closest_bar = min(
        bars,
        key=lambda bar: great_circle(my_coord, reversed(get_coordinates(bar))).km)
    return closest_bar


def get_seats_count(bar):
    return bar['properties']['Attributes']['SeatsCount']


def get_biggest_bar(bars):
    biggest_bar = max(
        bars,
        key=lambda bar: get_seats_count(bar)
    )
    return biggest_bar


def get_smallest_bar(bars):
    smallest_bar = min(
        bars,
        key=lambda bar: get_seats_count(bar)
    )
    return smallest_bar


def print_bar_attributes(text, bar):
    line = '=' * 80
    address = bar['properties']['Attributes']['Address']
    bar_name = bar['properties']['Attributes']['Name']
    seats_count = bar['properties']['Attributes']['SeatsCount']
    report_template = '{},\n Адрес {},\nНазвание {},\nКоличество мест {}\n{}'
    print(report_template.format(text, address, bar_name, seats_count, line))


def open_bars():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        bars = load_data(file_path)['features']
    else:
        site = 'https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json'
        bars = download_data(site)['features']
    return bars


if __name__ == '__main__':
    try:
        bars = open_bars()
        start_text = 'Введите широту и долготу. Для примера:\n55.754709, 37.618776\n'
        coordinates = input(start_text).split(', ')
        closest_bar = get_closest_bar(bars, coordinates)
        biggest_bar = get_biggest_bar(bars)
        smallest_bar = get_smallest_bar(bars)
        print_bar_attributes('Ближайший бар', closest_bar)
        print_bar_attributes('Самый большой бар', biggest_bar)
        print_bar_attributes('Самый маленький бар', smallest_bar)
    except FileNotFoundError:
        print('Неверно указан путь к файлу с барами. Запустите заново указав корректный путь к файлу')
    except requests.exceptions.ConnectionError:
        print('Нет соединение с интернетом. Запустите заново c указанием пути к файлу')
    except json.decoder.JSONDecodeError:
        print('Битый JSON файл')
    except ValueError:
        print('Запустите заново и введите корректные координаты. \nДля примера:55.754709, 37.618776\n')
