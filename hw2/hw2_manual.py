# Your code here!
from cse163_utils import assert_equals, parse


def species_count(data):
    species = set()
    for i in data:
        species.add(i['name'])
    return len(species)


def max_level(data):
    level = 0
    count = 0
    name = ''
    for i in data:
        curr_level = i['level']
        if curr_level >= level:
            level = curr_level
            name = i['name']
    for j in data:
        if j['level'] == level:
            count += 1
    if count > 1:
        return data[0]['name'], data[0]['level']
    return name, level


def filter_range(data, low, high):
    result = []
    for i in data:
        curr_level = i['level']
        if high > curr_level >= low:
            result.append(i['name'])
    return result


def mean_attack_for_type(data, type_name):
    temp = []
    for i in data:
        if i['type'] == type_name:
            temp.append(i['atk'])
    return sum(temp) / len(temp)


def count_types(data):
    dic = {}
    for i in data:
        curr_type = i['type']
        if curr_type not in dic:
            dic[curr_type] = 1
        else:
            dic[curr_type] += 1
    return dic


def mean_attack_per_type(data):
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
