from pprint import pprint

from faker import Factory
import string
import argparse
from faker.providers import lorem
import random

TWEET_LENGTH = 140
LINE_BREAK = '\n'


class TweetGenerator:

    def __init__(self, tweet_amount, break_symbol=None):
        """ Fake tweets Fabric. Realisation accept user break symbol

        Args:
            tweet_amount (int): How much tweets to generate
            break_symbol (str): Breaking symbol
        """
        self._tweets_counter = tweet_amount
        self._tweets = []
        self._break_symbol = (
                break_symbol if break_symbol is not None and
                                break_symbol in string.punctuation
                else LINE_BREAK
        )

    def __iter__(self):
        return self

    def create_tweet(self):
        """ Performing a fake tweet creation with custom or default breaks """
        fake = Factory.create()
        fake.add_provider(lorem)
        hashtag_picks = random.randint(0, 3)
        tweet_body = fake.text(max_nb_chars=80, ext_word_list=None)
        tweet_hashtags = (
            [f'#{hashtag} ' for hashtag in fake.words(
                nb=hashtag_picks,
                ext_word_list=None,
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

    def __str__(self):
        return str(len(self._tweets))

    def __repr__(self):
        return str(len(self._tweets))


if __name__ == '__main__':
    generator = TweetGenerator(50)
    for _ in generator:
        # This implementation give us space to correct
        # every tweet behaviour later (if needed)
        # Ex: Generating seed from random patterns
        pass
    pprint(generator._tweets)
