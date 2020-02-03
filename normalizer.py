import list

import tweet


def create():
    return Normalizer()


class Normalizer:
    def normalize(self, loaded: list) -> list:
        return self.__normalize_tweets(loaded)

    def __normalize_tweets(self, loaded: list) -> list:
        normalized = []
        for single_tweet in loaded:
            id = single_tweet['id']
            favorite_count = single_tweet['favorite_count']
            retweet_count = single_tweet['retweet_count']
            language = single_tweet['lang']
            country = self.__extract_country(single_tweet['geo'])
            user_loc = single_tweet['user']['location'] or "none"
            timezone = single_tweet['user']['time_zone'] or "none"
            created_at = single_tweet['created_at']
            tags = single_tweet['entities']['hashtags']
            text = single_tweet['text']

            normalized_tweet = tweet.create(
                id,
                retweet_count,
                favorite_count,
                country,
                user_loc,
                timezone,
                language,
                created_at,
                tags,
                text,
            )
            normalized.append(normalized_tweet)

        return normalized

    def __extract_country(self, object) -> str:
        if object is None:
            return "none"
        if object is dict:
            return object['country_code']
        return "none"

