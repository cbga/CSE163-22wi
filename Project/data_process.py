import csv
import os
import nltk
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import requests
from os.path import exists
# global variables across the files
global wt
global f


def auth():
    return os.getenv('TOKEN')


def get_headers(token):
    headers = {"Authorization": "Bearer {}".format(token)}
    return headers


def get_url(result_num=10, start_date='2022-03-03'):
    url = 'https://api.twitter.com/2/tweets/search/recent'
    params = {
        "query": ['covid -is:reply lang:en'],
        'end_time': start_date + 'T09:25:07.000Z',
        'max_results': result_num,
        'tweet.fields': 'text,created_at',
        'next_token': {}
    }
    return url, params


def connect_to_endpoint(url, headers, params, next_token=None):
    params['next_token'] = next_token
    response = requests.request("GET", url, headers=headers, params=params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def get_data(tweet_num, start_date):
    token = auth()
    headers = get_headers(token)
    target_num = tweet_num
    url, params = get_url(target_num, start_date)
    resp = connect_to_endpoint(url, headers, params)
    return resp


def write_data_in_csv(j_content):
    sia = SentimentIntensityAnalyzer()
    for tweet in j_content['data']:
        create_date = tweet['created_at'][:10]
        content = tweet['text'].replace(',', ' ')
        content_polar = sia.polarity_scores(content)
        content_polar_compound = content_polar.get('compound')
        if content_polar_compound >= 0:
            attitude = 'NON_negative'
        else:
            attitude = 'negative'
        tweet_info = [create_date, content, attitude]
        wt.writerow(tweet_info)


def init_csv_writer(path):
    global wt
    wt = csv.writer(path)
    wt.writerow(['created_at', 'text', 'attitude'])


def init_csv_file_and_writer(file_name):
    # Last change to input name
    global f
    if not exists(file_name):
        f = open(file_name, 'x', newline='', encoding="utf-8")
    f = open(file_name, 'w', newline='', encoding="utf-8")
    init_csv_writer(f)


# Filter the daily new cases by the same date as the tweets
def get_cases_by_day(df_cases):
    df_cases = df_cases[['Date_reported', 'New_cases']]
    df_cases = df_cases.groupby(by=['Date_reported']).sum()
    df_cases = df_cases.loc['2022-03-04':'2022-03-09']
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
        perc_neg = neg / tot
        res_dict[day] = perc_neg
    lsi = list(res_dict.items())
    df_attitude_by_day = pd.DataFrame(lsi)
    df_attitude_by_day.set_index([0], inplace=True)
    return df_attitude_by_day


def join_attitudes_and_cases(df_attitude, df_cases):
    merged = df_cases.join(df_attitude, how='left')
    merged = merged.rename(columns={1: 'Non-negative Percent'})
    return merged


def visualize(df_final):
    sns.lineplot(markers=True, data=df_final, x='New_cases',
                 y='Non-negative Percent')
    plt.title(
        'Relationship Between Daily New Cases and Non-negative Tweets about '
        'COVID-19',
        loc='center', wrap=True)
    plt.savefig('relationship.png')


def main():
    os.environ[
        'TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAHJRZQEAAAAA7dJCPjzhW7PhpmKz4EDKtga' \
                   '%2BmEQ%3DkwPq2w9tpjgMbPRYiYsH4rv2GV3tC0hSzP4Fk1WQ1zZ90O' \
                   'ZHbt'
    auth()
    nltk.download('vader_lexicon')
    df_cases = pd.read_csv('global-data-by-country-dat.csv')
    df_cases = get_cases_by_day(df_cases)
    csv_name = 'data.csv'
    init_csv_file_and_writer(csv_name)
    for date in df_cases.index.tolist():
        write_data_in_csv(get_data(100, date))
    print('... Done writing data!')
    f.close()
    df_tweet = pd.read_csv(csv_name)
    df_tweet.set_index('created_at', inplace=True)
    df_attitude = get_attitude_by_day(df_tweet)
    # combine two dataframe by their date
    joined_df = join_attitudes_and_cases(df_attitude, df_cases)
    visualize(joined_df)


if __name__ == '__main__':
    main()
