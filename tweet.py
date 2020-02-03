import datetime
import json

import dateutil.parser


def create(id: int,
           retweet_count: int,
           favourite_count: int,
           country: str,
           user_loc: str,
           timezone: str,
           language: str,
           created_at: str,
           hashtags: list,
           text: str
           ):
    tweet = Tweet()
    tweet.id = id
    tweet.retweet_count = retweet_count
    tweet.favourite_count = favourite_count
    tweet.country = country
    tweet.user_loc = user_loc
    tweet.timezone = timezone
    tweet.language = language
    tweet.created_at = dateutil.parser.parse(created_at)
    tweet.hashtags = tweet.extract_hashtags(hashtags)
    tweet.text = text

    return tweet




class Tweet:
    id: int
    retweet_count: int
    favourite_count: int
    country: str
    user_loc: str
    timezone: str
    language: str
    created_at: datetime.datetime
    hashtags = []
    text = []

    def from_json(self, json_data):
        loaded = json.loads(json_data)
        self.id = loaded['id']
        self.retweet_count = loaded['retweet_count']
        self.favourite_count = loaded['favourite_count']
        self.country = loaded['country']
        self.user_loc = loaded['user_loc']
        self.timezone = loaded['timezone']
        self.language = loaded['language']
        self.created_at = loaded['created_at']
        self.hashtags = loaded['hashtags']
        self.text = loaded['text']

        return self

    def as_dict(self) -> dict:
        return {
            'id': self.id,
            'retweet_count': self.retweet_count,
            'favourite_count': self.favourite_count,
            'country': self.country,
            'user_location': self.user_loc,
            'user_timezone': self.timezone,
            'language': self.language,
            'created_at': self.created_at,
            'hashtags': self.hashtags,
            'text': self.text,
        }

    def extract_hashtags(self, tags: list) -> list:
        hashtags = []
        for hashtag in tags:
            hashtags.append(hashtag['text'].lower())

        return hashtags