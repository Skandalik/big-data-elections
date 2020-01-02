import list
import os
import extractor
import saver
import tweet


def create(path):
    return Normalizer(path)


class Normalizer:
    __path: str
    __extractor: extractor.Extractor
    __saver: saver.Saver

    def __init__(self, path: str):
        self.__path = path
        save_path = '%s\\normalized_data' % os.getcwd()
        save_name = 'normalized_tweets'

        self.__extractor = extractor.create()
        self.__saver = saver.create(save_path, save_name)

    def normalize(self) -> list:
        loaded = self.__load_tweets(self.__path)
        normalized = self.__normalize_tweets(loaded)
        self.__saver.save(normalized)

        return normalized

    def __normalize_tweets(self, loaded: list) -> list:
        normalized = []
        for single_tweet in loaded:
            favorite_count = single_tweet['favorite_count']
            retweet_count = single_tweet['retweet_count']
            language = single_tweet['lang']
            country = single_tweet['geo'] or "none"
            user_loc = single_tweet['user']['location'] or "none"
            timezone = single_tweet['user']['time_zone'] or "none"
            created_at = single_tweet['created_at']
            tags = single_tweet['entities']['hashtags']

            normalized_tweet = tweet.Tweet(
                retweet_count,
                favorite_count,
                country,
                user_loc,
                timezone,
                language,
                created_at,
                tags
            )
            normalized.append(normalized_tweet)

        return normalized

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
