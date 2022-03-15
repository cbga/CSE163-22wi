import os
import settings
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import requests


def auth():
    return os.getenv('TOKEN')


def get_headers(token):
    headers = {"Authorization": "Bearer {}".format(token)}
    return headers


def get_url(result_num=10, start_date='2022-03-07'):
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
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    print('... find tweets saved')
    return response.json()


def get_data_as_json(tweet_num, start_date):
    token = auth()
    headers = get_headers(token)
    target_num = tweet_num
    url, params = get_url(target_num, start_date)
    # using api endpoint for specific data
    resp = connect_to_endpoint(url, headers, params)
    return resp


def write_data_from_data_to_csv(j_content):
    # use the trained model as an analyzer
    sia = SentimentIntensityAnalyzer()
    for tweet in j_content['data']:
        create_date = tweet['created_at'][:10]
        # avoid any comma so that the dataframe wouldn't perform
        #   in unexpected way.
        content = tweet['text'].replace(',', ' ')
        content_polar = sia.polarity_scores(content)
        content_polar_compound = content_polar.get('compound')
        if content_polar_compound >= 0:
            attitude = 'NON_negative'
        else:
            attitude = 'negative'
        tweet_info = [create_date, content, attitude]
        settings.wt.writerow(tweet_info)


# filter the daily new cases by the same date as the tweets
def get_cases_by_day(df_cases, start_day, end_day):
    df_cases = df_cases[['Date_reported', 'New_cases']]
    df_cases = df_cases.groupby(by=['Date_reported']).sum()
    df_cases = df_cases.loc[start_day:end_day]
    return df_cases


def add_tweets_data_to_cases():
    df_cases = pd.read_csv('WHO-COVID-19-global-data.csv')
    # ----------------------------------------
    # CHANGE start_day
    start_day = '2022-03-08'
    # CHANGE end_day
    end_day = '2022-03-13'
    # ----------------------------------------
    df_cases_shrinked = get_cases_by_day(df_cases, start_day, end_day)
    for date in df_cases_shrinked.index.tolist():
        write_data_from_data_to_csv(get_data_as_json(100, date))
    print('... added twitter data to cases data!')
    return df_cases_shrinked
