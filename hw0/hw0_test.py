import hw0

from cse163_utils import assert_equals


def test_total():
    # The regular case
    assert_equals(15, hw0.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw0.total(1))
    assert_equals(0, hw0.total(0))


def main():
    test_total()


if __name__ == '__main__':
    main()

