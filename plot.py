import load
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def create():
    return Plotter()


class Plotter:
    __loader: load.Loader

    def __init__(self):
        self.__loader = load.create('localhost', 6379)

    def plot(self):
        tweets = self.__loader.load()
        self.__plot_grouped(tweets)
        # self.__plot_by_date(tweets)
        # self.__plot_lang(tweets)

    def __plot_grouped(self, tweets):
        grouped = tweets[np.logical_or(tweets.hashtags.str.contains('hillary'), tweets.hashtags.str.contains('clinton'))].set_index('created_at').groupby(pd.Grouper(freq='D')).aggregate({'id': 'count'})
        # grouped = tweets[tweets.hashtags.str.contains('trump')].set_index('created_at').groupby(pd.Grouper(freq='D')).aggregate({'id': 'count'})

        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.plot_date(grouped.index.tolist(), grouped)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
        plt.show()

    def __plot_by_date(self, tweets):
        grouped = tweets.set_index('created_at').groupby(pd.Grouper(freq='D')).aggregate({'id': 'count'})

        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.plot_date(grouped.index.tolist(), grouped)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))

        fig.show()

    def __plot_lang(self, tweets):
        language = tweets.language[tweets.language != 'und']
        lang = language.value_counts()
        lang = lang[lang > 50]
        print(lang)

        plt.figure()
        plt.bar(lang.index.tolist(), lang)
        plt.show()
