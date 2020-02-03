import load
import matplotlib.pyplot as plt

def create():
    return Plotter()


class Plotter:
    __loader: load.Loader

    def __init__(self):
        self.__loader = load.create('localhost', 6379)

    def plot(self):
        tweets = self.__loader.load()
        language = tweets.language[tweets.language != 'und']
        print(language.value_counts())
        counts = language.value_counts()

        plt.figure()
        plt.bar(counts.index.tolist(), counts)
        plt.show()

