"""
Bingan Chen (AA)
Implements all functions required for hw3: Education. In this file,
the client can ask for comparing the bachelors degree from genders
in 1980, getting the 2 most commonly-awarded levels of educational
attainment awarded between 2000–2010 (inclusive) for a given sex,
plotting a line chart of the total percentages of all people with
a min bachelor degree, plotting the total percentages of different
genders with min high school degree, how the percentage of Hispanic
people with degrees have changed between 1990–2010 (inclusive) for
high school and bachelor's Min degree, and predicting the percentage
of Sex to achieve the Min degree in a given year based on the dataset
nces-ed-attainment.csv.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


sns.set()


def compare_bachelors_1980(data):
    """
    :param data: A DataFrame of the desired csv
    :return: A 2-by-2 DataFrame with rows corresponding to men and women
             and columns corresponding to Sex and Total.
    """
    df = data[data['Sex'] != 'A']
    after_mask = df[(df['Year'] == 1980) & (df['Min degree'] == 'bachelor\'s')]
    result = after_mask[['Sex', 'Total']]
    return result


def top_2_2000s(data, sex='A'):
    """
    :param data: A DataFrame of the desired csv file.
    :param sex: Specified sex. Default to 'A' if no sex parameter is specified
    :return: A 2-element Series, comparing mean educational attainment levels in
             specified sex.
    """
    mask = (2000 <= data['Year']) & (data['Sex'] == sex) & (data['Year'] <= 2010)
    df = data[mask]
    grouped = df.groupby('Min degree')['Total'].mean()
    return grouped.nlargest(2)


def line_plot_bachelors(data):
    """
    :param data: A DataFrame of the desired csv file.
    :return: None
    Save a figure named as line_plot_bachelors showing a line chart of the total
        percentages of all people Sex A with bachelor's Min degree over time.
    """
    data = data[(data['Sex'] == 'A') & (data['Min degree'] == 'bachelor\'s')]
    sns.relplot(data=data, x='Year', y='Total', kind='line')
    plt.ylabel('Percentage')
    plt.title('Percentage Earning Bachelor\'s over Time')
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def bar_chart_high_school(data):
    """
    :param data: A DataFrame of the desired csv file.
    :return: None
    Save a figure named as bar_chart_high_school comparing the total percentages
        of Sex F, M, and A with high school Min degree in the Year 2009.
    """
    data = data[(data['Year'] == 2009) & (data['Min degree'] == 'high school')]
    sns.catplot(data=data, x='Sex', y='Total', kind='bar', ci=None)
    plt.ylabel('Percentage')
    plt.title('Percentage Completed High School by Sex')
    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')


def plot_hispanic_min_degree(data):
    """
    :param data: A DataFrame of the desired csv file.
    :return: None
    Save a figure named as plot_hispanic_min_degree that shows how the percentage
        of Hispanic people with degrees have changed between 1990–2010
        (inclusive) for high school and bachelor's min degree.
    """
    mask1 = (data['Year'] >= 1990) & (data['Year'] <= 2010)
    mask2 = (data['Min degree'] == 'bachelor\'s') | (data['Min degree'] == 'high school')
    mask4 = data['Sex'] == 'A'
    data = data[mask1 & mask2 & mask4]
    sns.relplot(data=data, x='Year', y='Hispanic', kind='line', hue='Min degree')
    plt.ylabel('Percentage')
    plt.title('Percentage Hispanic People With Degree over Time')
    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')


def fit_and_predict_degrees(data):
    """
    :param data: A DataFrame of the desired csv file.
    :return: the test mean squared error as a float based on predicted the percentage
        of Sex to achieve the Min degree in a given Year.
    """
    data = data[['Year', 'Min degree', 'Sex', 'Total']]
    data = data.dropna()
    features = pd.get_dummies(data.loc[:, data.columns != 'Total'])
    labels = data['Total']
    features_train, features_test, labels_train, labels_test = train_test_split(
        features, labels, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)
    predictions = model.predict(features_test)
    error = mean_squared_error(labels_test, predictions)
    return error


def main():
    data = pd.read_csv('nces-ed-attainment.csv', na_values=['---'])
    compare_bachelors_1980(data)
    top_2_2000s(data)
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    fit_and_predict_degrees(data)


if __name__ == '__main__':
    main()
