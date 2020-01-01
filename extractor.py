import list
import json
import validator


def create():
    return Extractor()


class Extractor:
    __validator: validator.Validator

    def __init__(self):
        self.__validator = validator.create()

    def extract_tweets(self, raw: list) -> list:
        tweets = []
        for raw_tweet in raw:
            to_decode = r'%s' % raw_tweet
            decoded = json.loads(to_decode)
            if not self.__validator.validate(decoded):
                continue

            tweets.append(decoded)

        return tweets
