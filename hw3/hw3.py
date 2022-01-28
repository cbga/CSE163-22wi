import pandas as pd
import seaborn as sns
# Your imports here
sns.set()

# Define your functions here


def main():
    data = pd.read_csv('nces-ed-attainment.csv', na_values=['---'])
    # Call your functions here


if __name__ == '__main__':
    main()
