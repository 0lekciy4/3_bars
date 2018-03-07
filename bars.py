#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import sys
from geopy.distance import great_circle


def download_data(site):
    try:
        geted_site = requests.get(site)
        site_data = geted_site.json()
        return site_data
    except requests.exceptions.ConnectionError:
        sys.exit('Отсутствует соединение с интернетом')


def load_data(file_path):
    try:
        with open(file_path, 'r', encoding='UTF-8') as json_file:
            loaded_data = json.load(json_file)
        return loaded_data
    except FileNotFoundError:
        sys.exit('Некоректно указан путь к файлу')


def get_coordinates(bar):
    return bar.get('geometry').get('coordinates')


def get_name(bar):
    return bar.get('properties').get('Attributes').get('Name')


def get_address(bar):
    return bar.get('properties').get('Attributes').get('Address')


def get_seats_count(bar):
    return bar.get('properties').get('Attributes').get('SeatsCount')


def get_closest_bar(bars, my_coord):
    try:
        closest_bar = min(
            bars,
            key=lambda bar: great_circle(my_coord, reversed(get_coordinates(bar))).km)
        return closest_bar
    except ValueError:
        sys.exit('Некоректно введены координаты')


def get_bar_size(bars, compare_func):
    bar_size = compare_func(
        bars,
        key=lambda bar: get_seats_count(bar)
    )
    return bar_size


def print_line():
    line = '=' * 120
    print(line)


def open_bars():
    try:
        if len(sys.argv) > 1:
            file_path = sys.argv[1]
            bars = load_data(file_path)
        else:
            site = 'https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json'
            bars = download_data(site)
        return bars
    except json.decoder.JSONDecodeError:
        sys.exit('Битый JSON файл')


def get_user_coordinates():
    start_text = 'Введите широту и долготу. Для примера:\n55.754709, 37.618776\n'
    coordinates = input(start_text).split(', ')
    return coordinates


def main():
    bars = open_bars().get('features')
    coordinates = get_user_coordinates()
    selected_bars = {
        'Ближайший бар': get_closest_bar(bars, coordinates),
        'Самый большой бар': get_bar_size(bars, max),
        'Самый маленький бар': get_bar_size(bars, min)
    }
    for title, bar in selected_bars.items():
        print_line()
        print('{} - «{}» находится по адресу {} и там {} мест'.format(
            title, get_name(bar), get_address(bar), get_seats_count(bar)
        ))


if __name__ == '__main__':
    main()
