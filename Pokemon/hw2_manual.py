"""
Bingan Chen (AA
Implements functions for hw2 (manual)
"""


def species_count(data):
    """
    :param data: a parsed dataset
    ":return: the number of unique pokemon species in the dataset
    """
    species = set()
    for i in data:
        species.add(i['name'])
    return len(species)


def max_level(data):
    """
    :param data: a parsed dataset
    :return: a 2-element tuple of the (name, level) of the
             pokemon with the highest level in the dataset.
    """
    level = 0
    name = ''
    for pokemon in data:
        if pokemon['level'] > level:
            level = pokemon['level']
            name = pokemon['name']
    return name, level


def filter_range(data, low, high):
    """
    :param data: parsed dataset
    :param low: number of the lowest bound
    :param high: number of the highest bound
    :return: a list of the names of pokemon whose level fall within
             the bounds in the same order that they appear in the
             dataset.
    """
    result = []
    for i in data:
        curr_level = i['level']
        if high > curr_level >= low:
            result.append(i['name'])
    return result


def mean_attack_for_type(data, type_name):
    """
    :param data: parsed dataset
    :param type_name: the name of a desired name
    :return: the average atk for all the pokemon in the dataset with
             the given type
    """
    temp = []
    for i in data:
        if i['type'] == type_name:
            temp.append(i['atk'])
    if len(temp) == 0:
        return None
    return sum(temp) / len(temp)


def count_types(data):
    """
    :param data: parsed dataset
    :return: a dictionary representing for each pokemon type the
             number of pokemon of that type.
    """
    dic = {}
    for i in data:
        curr_type = i['type']
        if curr_type not in dic:
            dic[curr_type] = 1
        else:
            dic[curr_type] += 1
    return dic


def mean_attack_per_type(data):
    """
    :param data: parsed dataset
    :return: a dictionary representing for each pokemon type
             the average atk of pokemon of that type.
    """
    dic = {}
    for i in data:
        curr_type = i['type']
        if curr_type not in dic:
            dic[curr_type] = [i['atk']]
        else:
            dic[curr_type].append(i['atk'])
    for j in dic:
        dic[j] = sum(dic[j]) / len(dic[j])
    return dic
