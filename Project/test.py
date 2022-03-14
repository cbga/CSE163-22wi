import use_api_preprocess
import process_visualize
import cse163_utils
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


def test_cases_data(cases_df):
    pass


def test_ml_model(positive_st, negative_st):
    analyzer = SentimentIntensityAnalyzer()
    for pst in positive_st:
        polarity = analyzer.polarity_scores(pst)['compound']
        cse163_utils.assert_equals(True, polarity > 0)
    for ngt in negative_st:
        polarity = analyzer.polarity_scores(ngt)['compound']
        cse163_utils.assert_equals(True, polarity < 0)


def main():
    nltk.download('vader_lexicon')
    sentences = {'positive': ['Hello and good morning!', 'What a fantastic day', 'thank government for providing the test kits'], 'negative': ['What a terrible covid', 'I hate wearing mask add the day', 'What\'s wrong with this virus!']}
    test_ml_model(sentences.get('positive'), sentences.get('negative'))
    test_cases_file = '\\test\\test_case.csv'
    cases_df = pd.read_csv(test_cases_file)
    test_cases_data(cases_df)


if __name__ == '__main__':
    main()
