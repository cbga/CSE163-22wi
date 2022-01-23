import pandas as pd

from cse163_utils import assert_equals, parse

import hw2_manual
import hw2_pandas

# If you want to include more global constants,
# please check the code quality guide!
SPEC_TEST_FILE = "/home/pokemon_test.csv"

# Your tests here!
def test_data(data):
    print('Number of species:', hw2_manual.species_count(data))
    print('Highest level pokemon:', hw2_manual.max_level(data))
    print('Low-level Pokemon:', hw2_manual.filter_range(data, 1, 9))
    print('Average attack for fire types:', hw2_manual.mean_attack_for_type(data, 'fire'))
    print('Count of each Pokemon type:')
    print(hw2_manual.count_types(data))
    print('Average attack for each Pokemon type:')
    print(hw2_manual.mean_attack_per_type(data))


def main():
    spec_test_df = pd.read_csv(SPEC_TEST_FILE)  # a DataFrame
    spec_test_data = parse(SPEC_TEST_FILE)      # a list of dictionaries
    # Feel free to use these datasets in your tests!


if __name__ == '__main__':
    main()
