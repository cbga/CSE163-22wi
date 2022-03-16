import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def get_attitude_by_day(df_tweet):
    tweet_indexes = df_tweet.index.tolist()
    res_dict = {}
    for index in tweet_indexes:
        if index not in res_dict.keys():
            res_dict[index] = []
            attitude_for_day = df_tweet.loc[index, 'attitude']
            for attitude in attitude_for_day:
                res_dict[index].append(attitude)
    # percentage for non-negative comments in all for the day
    for day in res_dict.keys():
        single = res_dict[day]
        neg = 0
        tot = 0
        for sing_at in single:
            if sing_at == 'NON_negative':
                neg += 1
            tot += 1
        percent_negative = neg / tot
        res_dict[day] = percent_negative
    lsi = list(res_dict.items())
    df_attitude_by_day = pd.DataFrame(lsi)
    df_attitude_by_day.set_index([0], inplace=True)
    return df_attitude_by_day


def final_combined_data(twitter_df, df_cases):
    twitter_df.set_index('created_at', inplace=True)
    df_attitude = get_attitude_by_day(twitter_df)
    joined_data = df_cases.join(df_attitude, how='left')
    joined_data = joined_data.rename(columns={1: 'Non-negative Percent'})
    return joined_data


def visualize(df_final):
    print('Visualizing data... ')
    bar_chart_attitudes(df_final)
    line_cases(df_final)
    relation_reg(df_final)
    print('... visualizations finished.')


def bar_chart_attitudes(df_final):
    labels_attitude = df_final.index.values
    attitudes = df_final['Non-negative Percent'].array
    plt.bar(labels_attitude, attitudes)
    plt.title('People\'s Attitudes Toward COVID-19')
    plt.xlabel('Dates')
    plt.ylabel('Non-negative Percent')
    plt.savefig('output/attitudes.png')
    print('attitudes graph saved.')
    plt.close()


def line_cases(df_final):
    new_cases = df_final['New_cases'].array
    labels_case = df_final.index.values
    plt.plot(labels_case, new_cases)
    plt.title('Increased COVID-19 Cases Globally')
    plt.xlabel('Dates')
    plt.ylabel('Cases')
    plt.savefig('output/cases.png')
    print('cases graph saved.')
    plt.close()


def relation_reg(df_final):
    new_cases = df_final['New_cases'].array
    regressor = LinearRegression()
    X = new_cases.reshape(-1, 1)
    y = df_final['Non-negative Percent'].array
    regressor.fit(X, y)
    y_predict = regressor.predict(X)
    plt.scatter(X, y, color='blue')
    plt.plot(X, y_predict, color='red')
    plt.title(
        'Relationship Between Daily New Cases and Non-negative Tweets about '
        'COVID-19',
        loc='center', wrap=True)
    plt.savefig('output/relationship.png')
    print('relationship graph saved.')
    plt.close()
