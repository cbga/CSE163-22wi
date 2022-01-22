import pandas as pd

from cse163_utils import assert_equals, parse

import hw2_manual
import hw2_pandas

# If you want to include more global constants,
# please check the code quality guide!
SPEC_TEST_FILE = "/home/pokemon_test.csv"

# Your tests here!


def main():
    spec_test_df = pd.read_csv(SPEC_TEST_FILE)  # a DataFrame
    spec_test_data = parse(SPEC_TEST_FILE)      # a list of dictionaries
    # Feel free to use these datasets in your tests!


if __name__ == '__main__':
    main()
