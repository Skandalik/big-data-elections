import list


def create():
    return Validator()


class Validator:
    def validate(self, data: dict) -> bool:
        if list.key_exists("delete", data):
            return False

        return True
