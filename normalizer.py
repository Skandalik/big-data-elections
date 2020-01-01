import json
import list
import validator


def create(path):
    return Normalizer(path)


class Normalizer:
    path: str = ""
    validator: validator.Validator

    def __init__(self, path: str):
        self.path = path
        self.validator = validator.create()

    def normalize(self) -> list:
        raw = self.__load_tweets()
        tweets = self.__extract_tweets(raw)

        return tweets

    def __load_tweets(self) -> list:
        with open(self.path) as f:
            tweets_json = f.readlines()
        return list.strip_elements(tweets_json)

    def __extract_tweets(self, raw: list) -> list:
        tweets = []
        for raw_tweet in raw:
            to_decode = r'%s' % raw_tweet
            decoded = json.loads(to_decode)
            if not self.validator.validate(decoded):
                continue

            tweets.append(decoded)

        return tweets
