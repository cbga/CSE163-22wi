# Your code here!
import pandas as pd


def species_count(data):
    group = data.groupby('name')
    return len(group)


def max_level(data):
    max_val = data['level'].max()
    if len(data[data['level'] == max_val]) > 1:
        return data['name'][0], data['level'][0]
    data = data[data['level'] == max_val]
    for i in data['name']:
        for j in data['level']:
            return i, j


def filter_range(data, low, high):
    mask1 = data['level'] < high
    mask2 = data['level'] >= low
    data = data[mask1 & mask2]
    return list(data['name'])


def mean_attack_for_type(data, type_name):
    data = data[data['type'] == type_name]
    return data['atk'].mean()


def count_types(data):
    count = data['type'].value_counts()
    return dict(count)


def mean_attack_per_type(data):
    data = data.groupby('type')['atk'].mean()
    return dict(data)
