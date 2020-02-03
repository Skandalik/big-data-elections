import os

import fire
import process
import plot

filepath = '%s\\testdata\\nested' % os.getcwd()
batch_size = 10

class Commands(object):
    """Commands."""

    def process(self, path=filepath, batch=batch_size):
        processor = process.create(path)
        processor.scan()
        processor.process(batch)

    def plot(self):
        plotter = plot.create()
        plotter.plot()


if __name__ == '__main__':
    fire.Fire(Commands)
