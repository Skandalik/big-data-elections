import list
import os
import extractor


def create(path):
    return Normalizer(path)


class Normalizer:
    path: str = ""
    __extractor: extractor.Extractor

    def __init__(self, path: str):
        self.path = path
        self.__extractor = extractor.create()

    def normalize(self) -> list:
        loaded = self.__load_tweets(self.path)

        return loaded

    def __load_tweets(self, path: str) -> list:
        if os.path.isdir(path):
            tweets = []
            for single_dir in os.listdir(path):
                tweets = tweets + self.__load_tweets('%s\\%s' % (path, single_dir))

            return tweets

        return self.__load_and_extract(path)

    def __load_and_extract(self, path: str) -> list:
        with open(path) as f:
            tweets_json = f.readlines()
        stripped = list.strip_elements(tweets_json)
        extracted = self.__extractor.extract_tweets(stripped)

        return extracted
