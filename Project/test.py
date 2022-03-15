import use_api_preprocess
import cse163_utils
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


def test_cases_data(cases_df, start_day, end_day):
    expected = {
        'Date_reported': ['2000-01-01', '2000-02-01'], 'New_cases': [300, 140]
        }
    expected_df = pd.DataFrame(data=expected)
    expected_df.set_index('Date_reported', inplace=True)
    df_cases_after = use_api_preprocess.get_cases_by_day(
        cases_df, start_day, end_day
        )
    compare = df_cases_after.equals(expected_df)
    cse163_utils.assert_equals(True, compare)


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
    sentences = {
        'positive': [
            'Hello and good morning!',
            'What a fantastic day',
            'thank government for providing the test kits'
            ],
        'negative': [
            'What a terrible covid',
            'I hate wearing mask add the day',
            'What\'s wrong with this virus!'
            ]}
    test_ml_model(sentences.get('positive'), sentences.get('negative'))
    test_cases_file = 'test_files/test_case.csv'
    cases_df = pd.read_csv(test_cases_file)
    test_cases_data(cases_df, '2000-01-01', '2000-02-01')


if __name__ == '__main__':
    main()
