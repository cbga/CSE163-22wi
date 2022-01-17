def total(n):
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


# Write your functions here!
def count_divisible_digits(n, m):
    if n <= 0:
        return 1
    count = 0
    while n >= 0:
        num = n % 10
        if num % m == 0 or num == 0:
            count += 1
        n = n // 10
    return count


def is_relatively_prime(n, m):
    for i in range(2, n):
        if m % i == 0 and n % i == 0:
            return False
    return True


def travel(direction, x, y):
    x_new = x
    y_new = y
    for i in range(len(direction)):
        move = direction[i].lower()
        if move == 'n':
            y_new += 1
        elif move == 's':
            y_new -= 1
        elif move == 'e':
            x_new += 1
        elif move == 'w':
            x_new -= 1
    return x_new, y_new


def reformat_date(date, current, target):
    date_list = date.split('/')
    current_list = current.split('/')
    target_list = target.split('/')
    result_list = []
    dic = {}
    for i in range(len(date_list)):
        dic[current_list[i]] = date_list[i]
    for name in target_list:
        result_list.append(dic[name])
    return '/'.join(result_list)


def longest_word(file_name):
    dic = {}
    max_val = 0
    with open(file_name) as f:
        lines = f.readlines()
        if len(lines) == 0:
            return None
        for line in lines:
            for word in line.split():
                if word in dic:
                    dic[word.lower()] += 1
                else:
                    dic[word.lower()] = 1
                    first = word
                if dic[word.lower()] >= max_val:
                    max_val = dic[word.lower()]
                    max_word = first

    return str(max_val) + ': ' + max_word


def get_average_in_range(li, low, high):
    if len(li) == 0:
        return 0
    sum_num = 0
    count = 0
    for i in range(low, high):
        if i in li:
            sum_num += i
            count += 1
    return sum_num / count


def mode_digit(n):
    if n == 0:
        return 0
    n = abs(n)
    m = n
    unique = set()
    while n > 0:
        num = n % 10
        unique.add(num)
        n = n // 10
    dic = {}
    for i in unique:
        dic[i] = 0
    while m > 0:
        num = m % 10
        dic[num] += 1
        m = m // 10
    keys = []
    for key in dic:
        if dic[key] == max(dic.values()):
            keys.append(key)
    return max(keys)
