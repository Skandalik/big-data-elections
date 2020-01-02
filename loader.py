import os, printer
import counter, extractor, list
import bz2
import printer


def create(path: str):
    return Loader(path)


class Loader:
    count = 0

    __counter: counter.Counter
    __extractor: extractor.Extractor
    __path: str

    def __init__(self, path: str):
        self.__counter = counter.create()
        self.__extractor = extractor.create()
        self.__path = path

    def scan(self):
        self.__counter.scan(self.__path)
        self.__counter.success()

    def load(self) -> list:
        return self.__load_tweets(self.__path)

    def __load_tweets(self, path: str) -> list:
        if os.path.isdir(path):
            tweets = []
            for single_dir in os.listdir(path):
                tweets = tweets + self.__load_tweets('%s\\%s' % (path, single_dir))

            return tweets

        return self.__load_and_extract(path)

    def __load_and_extract(self, path: str) -> list:
        if not path.endswith('.bz2'):
            return []

        with open(path, 'rb') as source:
            decompressed = bz2.decompress(source.read()).split(b'\n')
            self.count += 1

        stripped = list.decode_elements(decompressed)
        extracted = self.__extractor.extract_tweets(stripped)
        printer.print("Decompressed %s of %s files. Processed %s JSONs." % (self.count, self.__counter.total, len(extracted)))

        return extracted
