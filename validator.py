import list
import pandas


def create():
    return Validator()


class Candidate:
    __name: str
    __surname: str

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def tags(self):
        return [
            self.__name,
            self.__surname,
            '%s%s' % (self.__name, self.__surname),
            'votefor%s' % self.__surname,
            'votefor%s%s' % (self.__name, self.__surname),
            'election',
            'elections',
        ]


class Validator:
    __candidates = [
        Candidate('donald', 'trump'),
        Candidate('mike', 'pence'),
        Candidate('hillary', 'clinton'),
        Candidate('tim', 'kaine'),
        Candidate('gary', 'johnson'),
        Candidate('bill', 'weld'),
        Candidate('jill', 'stein'),
        Candidate('ajamu', 'baraka'),
        Candidate('darrell', 'castle'),
        Candidate('scott', 'bradley'),
        Candidate('evan', 'mcmullin'),
        Candidate('mindy', 'finn'),
    ]

    def validate(self, data: dict) -> bool:
        if list.key_exists('delete', data):
            return False

        if not self.__tags_are_important(data):
            return False

        return True

    def __tags_are_important(self, data: dict) -> bool:
        if not list.key_exists('entities', data):
            return False

        if not list.key_exists('hashtags', data['entities']):
            return False

        for tag in data['entities']['hashtags']:
            if not list.key_exists('text', tag):
                continue

            if tag['text'].lower() not in self.__get_candidates_tags():
                continue

            return True

        return False

    def __get_candidates_tags(self) -> list:
        tags = []
        for candidate in self.__candidates:
            tags = tags + candidate.tags()

        return tags
