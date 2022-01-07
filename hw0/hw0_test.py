"""
Tests the methods (behaviors) for hw0.py
"""

import hw0
from cse163_utils import assert_equals


def test_funky_sum():
    """
    Test the method funky_sum(a, b, mix) in hw0.py
    """
    assert_equals(2.0, hw0.funky_sum(1, 3, 0.5))
    assert_equals(1, hw0.funky_sum(1, 3, 0))
    assert_equals(1.5, hw0.funky_sum(1, 3, 0.25))
    assert_equals(5, hw0.funky_sum(2, 5, 2))
    assert_equals(3.6, hw0.funky_sum(3, 4, 0.6))


def test_total():
    """
    Test the method total(n) in hw0.py
    """
    # The regular case
    assert_equals(15, hw0.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw0.total(1))
    assert_equals(0, hw0.total(0))


def test_swip_swap():
    """
    Test the method swip_swap(source, c1, c2) in hw0.py
    """
    assert_equals('offbar', hw0.swip_swap('foobar', 'f', 'o'))
    assert_equals('foocar', hw0.swip_swap('foobar', 'b', 'c'))
    assert_equals('foobar', hw0.swip_swap('foobar', 'z', 'c'))
    assert_equals('hallo', hw0.swip_swap('hello', 'e', 'a'))
    assert_equals('monrirg', hw0.swip_swap('morning', 'r', 'n'))


def main():
    test_total()
    test_funky_sum()
    test_swip_swap()


if __name__ == '__main__':
    main()
