"""
Tests the behaviors for hw2_pandas.py and hw2_manual.py
"""

import pandas as pd
from cse163_utils import assert_equals, parse
import hw2_manual
import hw2_pandas

# If you want to include more global constants,
# please check the code quality guide!
SPEC_TEST_FILE = "pokemon_test.csv"
OWN_TEST_FILE = "pokemon_own.csv"


def test_species_count(data, df, data_own, df_own):
    """
        Tests species_count in hw2_manual.py and hw2_pandas.py
    """
    assert_equals(3, hw2_manual.species_count(data))
    assert_equals(3, hw2_pandas.species_count(df))
    assert_equals(14, hw2_manual.species_count(data_own))
    assert_equals(14, hw2_pandas.species_count(df_own))


def test_max_level(data, df, data_own, df_own):
    """
        Tests max_level in hw2_manual.py and hw2_pandas.py
    """
    assert_equals(('Lapras', 72), hw2_manual.max_level(data))
    assert_equals(('Lapras', 72), hw2_pandas.max_level(df))
    assert_equals(('Arcanine', 87), hw2_manual.max_level(data_own))
    assert_equals(('Arcanine', 87), hw2_pandas.max_level(df_own))


def test_filter_range(data, df, data_own, df_own):
    """
        Tests filter_range in hw2_manual.py and hw2_pandas.py
    """
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_manual.filter_range(data, 35, 72))
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_pandas.filter_range(df, 35, 72))
    assert_equals(['Persian', 'Electabuzz', 'Poliwhirl', 'Hitmonlee'],
                  hw2_manual.filter_range(data_own, 10, 50))
    assert_equals(['Persian', 'Electabuzz', 'Poliwhirl', 'Hitmonlee'],
                  hw2_pandas.filter_range(df_own, 10, 50))


def test_mean_attack_for_type(data, df, data_own, df_own):
    """
        Tests mean_attack_for_type in hw2_manual.py and hw2_pandas.py
    """
    assert_equals(47.5, hw2_manual.mean_attack_for_type(data, 'fire'))
    assert_equals(47.5, hw2_pandas.mean_attack_for_type(df, 'fire'))
    assert_equals(91.2, hw2_manual.mean_attack_for_type(data_own, 'water'))
    assert_equals(91.2, hw2_pandas.mean_attack_for_type(df_own, 'water'))


def test_count_types(data, df, data_own, df_own):
    """
        Tests count_types in hw2_manual.py and hw2_pandas.py
    """
    assert_equals({'fire': 2, 'water': 2}, hw2_manual.count_types(data))
    assert_equals({'fire': 2, 'water': 2}, hw2_pandas.count_types(df))
    assert_equals({'water': 5, 'normal': 2, 'fire': 2, 'fighting': 2,
                   'fairy': 1, 'ghost': 1, 'flying': 1, 'electric': 1},
                  hw2_manual.count_types(data_own))
    assert_equals({'water': 5, 'normal': 2, 'fire': 2, 'fighting': 2,
                   'fairy': 1, 'ghost': 1, 'flying': 1, 'electric': 1},
                  hw2_pandas.count_types(df_own))


def test_mean_attack_per_type(data, df, data_own, df_own):
    """
        Tests mean_attack_per_type in hw2_manual.py and hw2_pandas.py
    """
    assert_equals({'fire': 47.5, 'water': 140.5},
                  hw2_manual.mean_attack_per_type(data))
    assert_equals({'fire': 47.5, 'water': 140.5},
                  hw2_pandas.mean_attack_per_type(df))
    assert_equals({'electric': 64.0, 'fairy': 92.0, 'fighting': 139.5,
                   'fire': 134.5, 'flying': 44.0, 'ghost': 54.0,
                   'normal': 70.5, 'water': 91.2},
                  hw2_manual.mean_attack_per_type(data_own))
    assert_equals({'electric': 64.0, 'fairy': 92.0, 'fighting': 139.5,
                   'fire': 134.5, 'flying': 44.0, 'ghost': 54.0,
                   'normal': 70.5, 'water': 91.2},
                  hw2_pandas.mean_attack_per_type(df_own))


def main():
    df = pd.read_csv(SPEC_TEST_FILE)  # a DataFrame
    data = parse(SPEC_TEST_FILE)  # a list of dictionaries
    df_own = pd.read_csv(OWN_TEST_FILE)
    data_own = parse(OWN_TEST_FILE)
    # Feel free to use these datasets in your tests!
    test_species_count(data, df, data_own, df_own)
    test_max_level(data, df, data_own, df_own)
    test_filter_range(data, df, data_own, df_own)
    test_mean_attack_for_type(data, df, data_own, df_own)
    test_count_types(data, df, data_own, df_own)
    test_mean_attack_per_type(data, df, data_own, df_own)


if __name__ == '__main__':
    main()
