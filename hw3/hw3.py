import pandas as pd
import seaborn as sns

# Your imports here
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import OneHotEncoder


sns.set()


# Define your functions here
def compare_bachelors_1980(data):
    df = data[data['Sex'] != 'A']
    after_mask = df[(df['Year'] == 1980) & (df['Min degree'] == 'bachelor\'s')]
    result = after_mask[['Sex', 'Total']]
    return result


def top_2_2000s(data, sex):
    mask = (2000 <= data['Year']) & (data['Sex'] == sex) & (data['Year'] <= 2010)
    df = data[mask]
    grouped = df.groupby('Min degree')['Total'].mean()
    return grouped.nlargest(2)


def line_plot_bachelors(data):
    data = data[(data['Sex'] == 'A') & (data['Min degree'] == 'bachelor\'s')]
    sns.relplot(data=data, x='Year', y='Total', kind='line')
    plt.ylabel('Percentage')
    plt.title('Percentage Earning Bachelor’s over Time')
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def bar_chart_high_school(data):
    data = data[(data['Year'] == 2009) & (data['Min degree'] == 'high school')]
    sns.catplot(data=data, x='Sex', y='Total', kind='bar', ci=None)
    plt.ylabel('Percentage')
    plt.title('Percentage Completed High School by Sex')
    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')


def plot_hispanic_min_degree(data):
    mask1 = (data['Year'] >= 1990) & (data['Year'] <= 2010)
    mask2 = (data['Min degree'] == 'bachelor\'s') | (data['Min degree'] == 'high school')
    mask3 = data['Hispanic'] != 'NaN'
    data = data[mask1 & mask2 & mask3]
    sns.relplot(data=data, x='Year', y='Total', kind='line', hue='Min degree')
    plt.ylabel('Percentage')
    plt.title('Percentage Hispanic People With Degree over Time')
    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')


def fit_and_predict_degrees(data):
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
    # Call your functions here
    compare_bachelors_1980(data)
    top_2_2000s(data, 'A')
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    print(fit_and_predict_degrees(data))


if __name__ == '__main__':
    main()
