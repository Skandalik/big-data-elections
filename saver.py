import os

import jsons


def create(path: str, filename: str):
    return Saver(path, filename)


class Saver:
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
