import json

from geopy.distance import great_circle


def load_data(filepath):
    with open(filepath, 'r', encoding='UTF-8') as json_file:
        json_data = json.load(json_file)
    return json_data


def get_coordinates(bar):
    return bar["geometry"]["coordinates"]


def get_closest_bar(bars_json, my_coord):
    closest_bar = min(bars_json, key=lambda bar: great_circle(my_coord, reversed(get_coordinates(bar))).km)
    return closest_bar


def get_seats_count(bar):
    return bar['properties']['Attributes']['SeatsCount']


def get_biggest_bar(bars_json):
    biggest_bar = max(
        bars_json,
        key=lambda bar: get_seats_count(bar)
    )
    return biggest_bar


def get_smallest_bar(bars_json):
    smallest_bar = min(
        bars_json,
        key=lambda bar: get_seats_count(bar)
    )
    return smallest_bar


def pretty_print_attributes(text, bar):
    address = bar['properties']['Attributes']['Address']
    name = bar['properties']['Attributes']['Name']
    seats_count = bar['properties']['Attributes']['SeatsCount']
    line = '============================================================'
    print('{},\n Адрес {},\nНазвание {},\nКоличество мест {}\n{}'.format(text, address, name,
                                                                         seats_count, line))


if __name__ == '__main__':
    bars_json = load_data('bars.json')['features']
    start_text = 'Введите широту и долготу, разделив их \",\". для примера:\n55.754709, 37.618776\n'
    coordinates = input(start_text).split(', ')
    closest_bar = get_closest_bar(bars_json, coordinates)
    biggest_bar = get_biggest_bar(bars_json)
    smallest_bar = get_smallest_bar(bars_json)
    pretty_print_attributes('Ближайший бар', closest_bar)
    pretty_print_attributes('Самый большой бар', biggest_bar)
    pretty_print_attributes('Самый маленький бар', smallest_bar)
