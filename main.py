import os

import fire
import process
import plotter

filepath = '%s\\..\\Dane twittera' % os.getcwd()
batch_size = 100

class Commands(object):
    """Simple strategy for Commands."""

    def process(self, path=filepath):
        processor = process.create(path)
        processor.scan()
        processor.process(batch_size)

    def plot(self, options=""):
        return plotter.plot()


if __name__ == '__main__':
    fire.Fire(Commands)
