import os

import fire
import process
import plotter

filepath = '%s\\testdata\\nested' % os.getcwd()
batch_size = 10

class Commands(object):
    """Commands."""

    def process(self, path=filepath, batch=batch_size):
        processor = process.create(path)
        processor.scan()
        processor.process(batch)

    # TODO: do plotting
    def plot(self, options=""):
        return plotter.plot()


if __name__ == '__main__':
    fire.Fire(Commands)
