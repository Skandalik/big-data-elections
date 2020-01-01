import json


def normalize(path):
    tweets = __get_tweets__(path)
    sanitized = sanitize(tweets)

    return 'Normalizing data with path %s' % path


def sanitize(tweets):
    for tweet in tweets:
        if not __key_exists__("delete", tweet):
            continue
        tweets.remove(tweet)
    return tweets


def __key_exists__(key, dictionary):
    return key in dictionary.keys()


def __get_tweets__(path):
    with open(path) as f:
        tweets_json = f.readlines()
    tweets_json = __strip_elements__(tweets_json)

    tweets = []
    for tweet in tweets_json:
        to_decode = r'%s' % tweet
        tweets.append(json.loads(to_decode))

    return tweets


def __strip_elements__(data):
    return [x.strip() for x in data]
