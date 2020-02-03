import os

import jsons
import redis

redis_saver = 'redis'

def create(host: str, port: int):
    return Redis(host, port)


class Redis:
    __tweets: str = 'tweets'
    __redis: redis.Redis

    def __init__(self, host: str, port: int):
        self.__redis = redis.Redis(host=host, port=port)

    def save(self, tweets: list):
        for tweet in tweets:
            self.__redis.hset(self.__tweets, tweet.id, jsons.dumps(tweet))

    def get_all(self):
        return self.__redis.hgetall(self.__tweets)
