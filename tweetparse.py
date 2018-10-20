from collections import Counter
import re
from pprint import pprint


def parse_input_file(filepath):
    words = re.findall(r'#(\w+)', open(filepath).read())
    popular_tweets = {
        word: Counter() for word in dict(Counter(words).most_common(10)).keys()
    }

    #
    print(f'The most common hashtags are - '
          f'{", ".join(list(popular_tweets.keys()))}')
    #
    print(f'Verification output - {Counter(words).most_common(10)}\n')

    # Any character combination except \n (new line)
    tweets = re.findall(r'.+', open(filepath).read())
    # List comp is used because of best readability (it's working slower btw)
    # There where no words about speed and accuracy, only about readability
    # In case of real project it is better to use map or generator
    [
        popular_tweets[word].update(
            Counter(
                re.findall(r'(\w+)', tweet.replace(f'#{word}', ''))
            )
        )
        for word in popular_tweets.keys()
        for tweet in tweets if f'#{word}' in tweet
    ]
    top_five_words_for_tags = {
        key: list(dict(popular_tweets[key].most_common(5)).keys())
        for key in popular_tweets.keys()
    }
    #
    print(f'Top five of most common words for twits - ')
    pprint(top_five_words_for_tags)
    #
    top_five_words_for_tags_verification = {
        key: (popular_tweets[key].most_common(5))
        for key in popular_tweets.keys()
    }
    print(f'\nVerification output - {top_five_words_for_tags_verification}')


parse_input_file('in.txt')