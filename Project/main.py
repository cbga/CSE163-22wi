from ast import keyword
import csv
from email import header
from os.path import exists
import os
from this import d
import geopandas as gpd
from matplotlib.pyplot import connect
import pandas as pd
import requests
import json
import datetime


os.environ['TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAHJRZQEAAAAA7dJCPjzhW7PhpmKz4EDKtga%2BmEQ%3DkwPq2w9tpjgMbPRYiYsH4rv2GV3tC0hSzP4Fk1WQ1zZ90OZHbt'


def auth():
    return os.getenv('TOKEN')


def get_headers(token):
    headers = {"Authorization": "Bearer {}".format(token)}
    return headers


def get_url(result_num=10):
    url = 'https://api.twitter.com/2/tweets/search/recent'
    params = {
        "query":['covid -is:reply'],
        'max_results': result_num,
        'expansions': 'geo.place_id',
        'tweet.fields': 'id,text,author_id,geo',
        'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
        'next_token': {}
    }
    return url, params


def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token
    response = requests.request("GET", url, headers=headers, params=params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def get_data(tweet_num):
    token = auth()
    headers = get_headers(token)
    target_num = tweet_num
    url, params = get_url(target_num)
    resp = connect_to_endpoint(url, headers, params)
    return resp


def write_data_in_csv(j_content):
    counter = 0
    for tweet in j_content['data']:
        id = tweet['id']
        text = tweet['text']
        if 'geo' in tweet:
            geo = tweet['geo']['place_id']
            coo = tweet['geo'].coordinates.coordinates
        else:
            geo = ''
            coo = ''
        tweet_info = [id, text, geo, coo]
        wt.writerow(tweet_info)
        counter += 1
    print('已收集数据：', counter)
    f.close()

def init_csv_writer(path):
    global wt
    wt = csv.writer(path)
    


def init_csv_file_and_writer(file_name):
    # Last change to input name
    global f
    if not exists(file_name):
        f = open(file_name, 'x', newline='')
    f = open(file_name, 'a', newline='')
    init_csv_writer(f)


def process_data(dataframe):
    return dataframe.dropna()


def draw_density(file):
    pass


def main():
    csv_name = 'data.csv'
    init_csv_file_and_writer(csv_name)
    wt.writerow(['id', 'text', 'geo', 'cood'])
    net_data = get_data(100)
    write_data_in_csv(net_data)
    df = pd.read_csv(csv_name)
    df = process_data(df)
    print(df.head())

if __name__ == '__main__':
    main()