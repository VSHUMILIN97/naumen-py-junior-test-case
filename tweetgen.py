from pprint import pprint

from faker import Factory
import string
import argparse
from faker.providers import lorem
import random
# Bad practice, but I did __all__ after all
from word_list import *


# Constants for excluding hardcode redundancy
TWEET_LENGTH = 140
LINE_BREAK = '\n'

__all__ = (
    'TWEET_LENGTH',
    'LINE_BREAK',
    'TweetGenerator',
    'GenerationException',
)


class GenerationException(Exception):
    """ Custom Exception for the TweetGenerator
        Raise when tweets where not generated
    """


class TweetGenerator:

    def __init__(self, tweet_amount, break_symbol=None):
        """ Fake tweets fabric. It is possible to use user's break symbol

        Args:
            tweet_amount (int): How much tweets to generate
            break_symbol (str): Breaking symbol
        """
        # Blocking memory overusing
        self._tweets_counter = tweet_amount if tweet_amount < 10000 else 500
        self._tweets = []
        self._break_symbol = (
                break_symbol if break_symbol is not None and
                                break_symbol in string.punctuation
                else LINE_BREAK
        )
        self.__inner_count = tweet_amount

    def __iter__(self):
        return self

    def create_tweet(self):
        """ Performing a fake tweet creation with custom or default breaks """
        fake = Factory.create()
        fake.add_provider(lorem)
        hashtag_picks = random.randint(0, 3)
        # Use BODYTEXT instead of None for less spreading in word generation
        tweet_body = fake.text(max_nb_chars=80, ext_word_list=None)
        tweet_hashtags = (
            [f'#{hashtag} ' for hashtag in fake.words(
                nb=hashtag_picks,
                ext_word_list=None,  # Use HASHTAGS for the same reason
                unique=False
            )]
        )
        tweet = "".join(tweet_hashtags)
        tweet += tweet_body
        self._tweets.append(self.check_and_correct_fake_tweet(tweet))

    def check_and_correct_fake_tweet(self, tweet):
        """ Checking whether fake tweet is OK or have to be treated
            (The easiest way)

        Args:
            tweet (str): Raw tweet which can be > 140 symbols and with
                         incorrect line separator

        Returns:
            tweet (str): Tweet which is less than 140 symbols and
                         have a correct line separator
        """
        if 0 >= len(tweet) > TWEET_LENGTH:
            tweet = 'Mock me. #NotWorkingWellWithRandom' + self._break_symbol
        return tweet + self._break_symbol

    def __next__(self):
        """ Creating a tweet via iterator """
        if self._tweets_counter == 0:
            raise StopIteration
        self.create_tweet()
        self._tweets_counter -= 1
        # Friendly UI :)
        if self._tweets_counter % 30 == 0:
            percent_done = format(
                round((1 - self._tweets_counter / self.__inner_count) * 100, 2)
            )
            return (f'Work in progress....'
                    f'{percent_done}%'
                    ' percents done')

    def create_output_file(self):
        """ Tweet file generation. Output file will be stored
            in the same directory where script stored.
        """
        if self._tweets_counter != 0 or len(self._tweets) == 0:
            raise GenerationException('No tweets generated')
        try:
            with open('in.txt', 'w+') as file:
                file.write("".join(self._tweets))
        except OSError:
            raise OSError(
                "File wasn't written. Check dir (write) permissions"
            )

    def __str__(self):
        return str(len(self._tweets))

    def __repr__(self):
        return str(len(self._tweets))


def parse_args():
    """ Standard realisation of parsing args from console input """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'tweet_number',
        type=int,
        help=(
            'Integer value. Input how much tweets you want to generate. '
            'If you will try to generate over 10000 tweets '
            'script will pick 500 as default.'
        ),
    )
    parser.add_argument(
        '--separator',
        type=str,
        help='String value. Separator between tweets',
    )
    return parser.parse_args()


if __name__ == '__main__':
    arguments = parse_args()
    generator = TweetGenerator(arguments.tweet_number, arguments.separator)
    for msg in generator:
        # This implementation give us space to correct
        # every tweet behaviour later (if needed)
        # Ex: Generating seed from random patterns
        if msg is not None:
            pprint(msg)
        else:
            pass
    generator.create_output_file()
