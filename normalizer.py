import list
import os
import loader
import saver
import tweet


def create(path):
    return Normalizer(path)


class Normalizer:
    __loader: loader.Loader
    __saver: saver.Saver

    def __init__(self, path: str):
        save_path = '%s\\normalized_data' % os.getcwd()
        save_name = 'normalized_tweets'

        self.__saver = saver.create(save_path, save_name)
        self.__loader = loader.create(path)

    def normalize(self) -> list:
        loaded = self.__loader.scan().load()
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
