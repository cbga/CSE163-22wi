import process_visualize
import use_api_preprocess
import settings
import os
import nltk
import pandas as pd


def main():
    twitter_data_csv = 'data.csv'
    os.environ[
        'TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAHJRZQEAAAAA7dJCPjzhW7PhpmKz4EDKtga' \
                   '%2BmEQ%3DkwPq2w9tpjgMbPRYiYsH4rv2GV3tC0hSzP4Fk1WQ1zZ90O' \
                   'ZHbt'
    use_api_preprocess.auth()
    settings.init('data.csv')
    settings.wt.writerow(['created_at', 'text', 'attitude'])
    nltk.download('vader_lexicon')
    cases_shrinked_df = use_api_preprocess.add_tweets_data_to_cases()
    settings.f.close()
    df_tweet = pd.read_csv(twitter_data_csv)
    joined_df = process_visualize.final_combined_data(
        df_tweet, cases_shrinked_df)
    print(joined_df)
    process_visualize.visualize(joined_df)


if __name__ == '__main__':
    main()
