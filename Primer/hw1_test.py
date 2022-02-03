"""
Bingan Chen (AA)
Tests functions in hw1 (hw1.py).
"""

import hw1

from cse163_utils import assert_equals


def test_total():
    """
    Tests the total method
    """
    # The regular case
    assert_equals(15, hw1.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw1.total(1))
    assert_equals(0, hw1.total(0))

    # Test the None case
    assert_equals(None, hw1.total(-1))


def test_count_divisible_digits():
    """
    Tests the count_divisible_digits method
    """
    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    assert_equals(0, hw1.count_divisible_digits(24, 5))
    assert_equals(0, hw1.count_divisible_digits(1, 0))
    # additional
    assert_equals(5, hw1.count_divisible_digits(99999, 3))
    assert_equals(2, hw1.count_divisible_digits(600, 8))


def test_is_relatively_prime():
    """
    Tests the is_relatively_prime method
    """
    assert_equals(True, hw1.is_relatively_prime(12, 13))
    assert_equals(False, hw1.is_relatively_prime(12, 14))
    assert_equals(True, hw1.is_relatively_prime(5, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 1))
    # additional
    assert_equals(False, hw1.is_relatively_prime(81, 72))
    assert_equals(False, hw1.is_relatively_prime(3, 3))


def test_travel():
    """
    Tests the travel method
    """
    assert_equals((-1, 4), hw1.travel('NW!ewnW', 1, 2))
    # additional
    assert_equals((2, 3), hw1.travel('!!!!!!00022!?', 2, 3))
    assert_equals((4, 2), hw1.travel('eeeEnnN!s', 0, 0))


def test_reformat_date():
    """
    Tests the reformat_date method
    """
    assert_equals("3/1/2", hw1.reformat_date('1/2/3', 'M/D/Y', 'Y/M/D'))
    assert_equals("4/0", hw1.reformat_date('0/200/4', 'Y/D/M', 'M/Y'))
    assert_equals("2", hw1.reformat_date('3/2', 'M/D', 'D'))
    assert_equals("31/12/1998", hw1.reformat_date(
        "12/31/1998", "M/D/Y", "D/M/Y"))
    # additional
    assert_equals("1/17/2022", hw1.reformat_date(
        '2022/1/17', 'Y/M/D', 'M/D/Y'))
    assert_equals("1", hw1.reformat_date('2022/1/17', 'Y/M/D', 'M'))


def test_longest_word():
    """
    Tests the longest_word method
    """
    assert_equals('3: Merrily,', hw1.longest_word('song.txt'))
    # additional
    assert_equals('13: beautiful!', hw1.longest_word('second_song.txt'))
    assert_equals('6: master,', hw1.longest_word('third_song.txt'))


def test_get_average_in_range():
    """

    Tests the get_average_in_range method
    """
    assert_equals(5.5, hw1.get_average_in_range([1, 5, 6, 7, 9], 5, 7))
    assert_equals(2.0, hw1.get_average_in_range([1, 2, 3], -1, 10))
    # additional
    assert_equals(0, hw1.get_average_in_range([], 1, 100))
    assert_equals(-2.0, hw1.get_average_in_range([-1, -3, -5, 87], -4, 0))
    assert_equals(0, hw1.get_average_in_range([], -4, 0))
    assert_equals(0, hw1.get_average_in_range([-8, -9], -4, 0))


def test_mode_digit():
    """
    Tests the mode_digit method
    """
    assert_equals(1, hw1.mode_digit(12121))
    assert_equals(0, hw1.mode_digit(0))
    assert_equals(2, hw1.mode_digit(-122))
    assert_equals(2, hw1.mode_digit(1211232231))
    # additional
    assert_equals(0, hw1.mode_digit(100000))
    assert_equals(9, hw1.mode_digit(-8967509988))


def main():
    test_total()
    test_mode_digit()
    test_travel()
    test_get_average_in_range()
    test_longest_word()
    test_count_divisible_digits()
    test_reformat_date()
    test_is_relatively_prime()
    # Call your test functions here!


if __name__ == '__main__':
    main()
