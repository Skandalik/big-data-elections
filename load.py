import pandas as pd

import connector
import tweet


def create(host: str, port: int):
    return Loader(host, port)


class Loader:
    __redis: connector.Redis

    def __init__(self, host: str, port: int):
        self.__redis = connector.create(host=host, port=port)

    def load(self):
        json_tweets = self.__redis.get_all()
        tweets = []
        for json_id, json_tweet in json_tweets.items():
            loaded = tweet.Tweet().from_json(json_tweet)
            tweets.append(loaded)

        df = pd.DataFrame([t.as_dict() for t in tweets])
        df['created_at'] = pd.to_datetime(df['created_at'])

        return df
