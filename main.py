import os

import fire
import normalizer
import plotter

filepath = '%s\\testdata\\tweets.json' % os.getcwd()


class Commands(object):
    """Simple strategy for Commands."""

    def normalize(self, path=filepath):
        return normalizer.normalize(path)

    def plot(self, options=""):
        return plotter.plot()


if __name__ == '__main__':
    fire.Fire(Commands)