import json
import sys
from geopy.distance import great_circle


def load_data(file_path):
    with open(file_path, 'r', encoding='UTF-8') as json_file:
        loaded_json = json.load(json_file)
    return loaded_json


def get_coordinates(bar):
    return bar['geometry']['coordinates']


def get_name(bar):
    return bar['properties']['Attributes']['Name']


def get_address(bar):
    return bar['properties']['Attributes']['Address']


def get_seats_count(bar):
    return bar['properties']['Attributes']['SeatsCount']


def get_closest_bar(bars, my_coord):
    closest_bar = min(
        bars,
        key=lambda bar: great_circle(my_coord, reversed(get_coordinates(bar))).km)
    return closest_bar


def get_extremum_seats_count(bars, compare_func):
    bar_size = compare_func(
        bars,
        key=lambda bar: get_seats_count(bar)
    )
    return bar_size


def print_delimiter():
    delimiter = '=' * 80
    print(delimiter)


def get_user_coordinates():
    start_text = 'Введите широту и долготу. Для примера:\n55.754709, 37.618776\n'
    coordinates = input(start_text).split(', ')
    return coordinates


def main():
    try:
        bars = load_data(sys.argv[1])['features']
        coordinates = get_user_coordinates()
        selected_bars = {
            'Ближайший бар': get_closest_bar(bars, coordinates),
            'Самый большой бар': get_extremum_seats_count(bars, max),
            'Самый маленький бар': get_extremum_seats_count(bars, min)
        }
        for title, bar in selected_bars.items():
            print_delimiter()
            print('{} - «{}» находится по адресу {} и там {} мест'.format(
                title, get_name(bar), get_address(bar), get_seats_count(bar)
            ))
    except json.decoder.JSONDecodeError:
        print('Битый JSON файл')
    except ValueError:
        print('Некоректно введены координаты')
    except (FileNotFoundError, IndexError):
        print('Некоректно указан путь к файлу')


if __name__ == '__main__':
    main()
