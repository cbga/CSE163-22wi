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
    if m == 0:
        return 0
    if n <= 0:
        return 1
    count = 0
    while n > 0:
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
    line_num = 0
    max_line = 0
    longest_word = ''
    with open(file_name) as f:
        for line in f.readlines():
            line_num += 1
            for word in line.split():
                if len(word) > len(longest_word):
                    max_line = line_num
                    longest_word = word
    if longest_word == '':
        return None
    return str(max_line) + ': ' + longest_word


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
