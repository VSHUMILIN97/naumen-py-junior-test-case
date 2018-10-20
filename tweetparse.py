import argparse
from collections import Counter
import re
from pprint import pprint
import os


def is_file_valid(filepath):
    """ Function checks whether file is OK or not (also verify UTF-8)

    Returns:
        filepath: Path to file.

    Notes:
        Path to file will be returned only if no errors occurred
    """
    if not os.path.isfile(filepath):
        raise TypeError('Not file')
    if os.path.splitext(filepath)[-1].lower() != '.txt':
        raise TypeError('Not .txt file')
    try:
        with open(filepath, 'rb+') as file:
            file.read().decode('utf-8')
    except UnicodeDecodeError:
        return None
    return filepath


def parse_input_file(filepath):
    """ Function which extracts 10 most used hashtags from array of tweets and
        then finds 5 most used words for every hashtag from 10's list

    Args:
        filepath: path to file (*.txt)
    """
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
            # TODO: Make replace work only on copies of original tweets list
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


def parse_args():
    """ Standard realisation of parsing args from console input """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path',
        help='Provide path to file',
    )
    return parser.parse_args()


if __name__ == '__main__':
    parsed_args = parse_args()
    parse_input_file(is_file_valid(parse_args().path))

