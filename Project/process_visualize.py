import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def get_cases_by_day(df_cases):
    df_cases = df_cases[['Date_reported', 'New_cases']]
    df_cases = df_cases.groupby(by=['Date_reported']).sum()
    df_cases = df_cases.loc['2022-03-07':'2022-03-13']
    return df_cases


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
    sns.lineplot(markers=True, data=df_final, x='New_cases',
                 y='Non-negative Percent')
    plt.title(
        'Relationship Between Daily New Cases and Non-negative Tweets about '
        'COVID-19',
        loc='center', wrap=True)
    plt.savefig('relationship.png')
