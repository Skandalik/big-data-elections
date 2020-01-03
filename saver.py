import os

import jsons
import redis

file_saver = 'file'
redis_saver = 'redis'


def create_file_saver(path: str, filename: str):
    return FileSaver(path, filename)


class FileSaver:
    __filepath: str
    __extension: str = '.json'
    __count = 0

    def __init__(self, path, filename):
        self.__filepath = '%s\\%s' % (path, filename)
        self.count = 0

    def save(self, tweets: list):
        while self.__validate_name():
            self.count += 1

        with open(self.__get_custom_filepath(), 'w') as outfile:
            outfile.write(jsons.dumps(tweets))

    def __validate_name(self) -> bool:
        filepath = self.__get_custom_filepath()
        return os.path.isfile(filepath)

    def __get_custom_filepath(self) -> str:
        return '%s_%d%s' % (self.__filepath, self.count, self.__extension)


def create_redis_saver(host: str, port: int):
    return RedisSaver(host, port)


class RedisSaver:
    __tweets: str = 'tweets'
    __redis: redis.Redis

    def __init__(self, host: str, port: int):
        self.__redis = redis.Redis(host=host, port=port)

    def save(self, tweets: list):
        for tweet in tweets:
            self.__redis.hset(self.__tweets, tweet.get_id(), jsons.dumps(tweet))
