import datetime
import dateutil.parser


class Tweet:
    __id: int
    __retweet_count: int
    __favourite_count: int
    __country: str
    __user_loc: str
    __timezone: str
    __language: str
    __created_at: datetime.datetime
    __hashtags = []
    __text = []

    def __init__(self,
                 id: int,
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
        self.__id = id
        self.__retweet_count = retweet_count
        self.__favourite_count = favourite_count
        self.__country = country
        self.__user_loc = user_loc
        self.__timezone = timezone
        self.__language = language
        self.__created_at = dateutil.parser.parse(created_at)
        self.__hashtags = self.__extract_hashtags(hashtags)
        self.__text = text

    def get_id(self) -> int:
        return self.__id

    def __extract_hashtags(self, tags: list) -> list:
        hashtags = []
        for hashtag in tags:
            hashtags.append(hashtag['text'].lower())

        return hashtags
