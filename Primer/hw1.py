"""
Bingan Chen (AA)
Implements the function for hw1 Primer.
"""


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
    """
    Returns the number of digits in "n" that are divisible by "m"
    (0 <= m <= 10).
    If m = 0, returns 0.
    """
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
    """
    Returns if the numbers "n" and "m" share no common factors besides 1.
    """
    for i in range(2, n + 1):
        if m % i == 0 and n % i == 0:
            return False
    return True


def travel(direction, x, y):
    """
    Returns a tuple indicating the new position after following the
    "direction" starting from "x", "y". (case-insensative)
    Any character that doesn't indicate valid direction will be ignored.
    """
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
    """
    Returns a new string with the "date" formatted in the "target" format
    from the "current" format.
    """
    result = ''
    date_list = date.split('/')
    current_list = current.split('/')
    target_list = target.split('/')
    dic = {}
    for i in range(len(date_list)):
        dic[current_list[i]] = date_list[i]
    for j in range(len(target_list) - 1):
        result += dic[target_list[j]] + '/'
    return result + dic[target_list[-1]]


def longest_word(file_name):
    """
    Returns the longest word in the file ("file_name") with which
    line it appears on.
    If the file is empty or there are no words in the file, returns None.
    If there are ties for the longest word, it returns the one that
    appears first in the file.
    """
    line_num = 0
    max_line = 0
    the_longest = ''
    with open(file_name) as f:
        for line in f.readlines():
            line_num += 1
            for word in line.split():
                if len(word) > len(the_longest):
                    max_line = line_num
                    the_longest = word
    if the_longest == '':
        return None
    return str(max_line) + ': ' + the_longest


def get_average_in_range(li, low, high):
    """
    Returns the average of all values in list "li" in the range from "low"
    (inclusive) to "high" (exclusive).
    If there are no values in the given range, returns 0.
    """
    sum_num = 0
    count = 0
    for i in range(low, high):
        if i in li:
            sum_num += i
            count += 1
    if count == 0:
        return 0
    return sum_num / count


def mode_digit(n):
    """
    Returns the digit that appears most frequently in the number "n".
    Returns the digit with the great value if there is a tie of most
    frequent digits.
    """
    n = abs(n)
    dic = {}
    result = 0
    while n > 0:
        num = n % 10
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
        n = n // 10
    for i in dic:
        if dic[i] == max(dic.values()) and i >= result:
            result = i
    return result
