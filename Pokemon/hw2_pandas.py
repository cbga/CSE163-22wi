"""
Bingan Chen (AA
Implements functions for hw2 (with pandas)
"""


def species_count(data):
    """
    :param data:
    :return:
    """
    group = data.groupby('name')
    return len(group)


def max_level(data):
    """
    :param data: a parsed dataset
    :return: a 2-element tuple of the (name, level) of the
             pokemon with the highest level in the dataset.
    """
    level = data['level'].max()
    result = data.loc[data['level'].idxmax(), 'name']
    return result, level


def filter_range(data, low, high):
    """
    :param data: parsed dataset
    :param low: number of the lowest bound
    :param high: number of the highest bound
    :return: a list of the names of pokemon whose level fall within
             the bounds in the same order that they appear in the
             dataset.
    """
    data = data[(data['level'] < high) & (data['level'] >= low)]
    return list(data['name'])


def mean_attack_for_type(data, type_name):
    """
    :param data: parsed dataset
    :param type_name: the name of a desired name
    :return: the average atk for all the pokemon in the dataset with
             the given type
    """
    data = data[data['type'] == type_name]
    if len(data) == 0:
        return None
    return data['atk'].mean()


def count_types(data):
    """
        :param data: parsed dataset
        :return: a dictionary representing for each pokemon type the
                 number of pokemon of that type.
    """
    count = data['type'].value_counts()
    return dict(count)


def mean_attack_per_type(data):
    """
        :param data: parsed dataset
        :return: a dictionary representing for each pokemon type
                 the average atk of pokemon of that type.
    """
    data = data.groupby('type')['atk'].mean()
    return dict(data)
