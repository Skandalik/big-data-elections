def key_exists(key, dictionary):
    return key in dictionary.keys()


def decode_elements(data):
    return [x.decode('utf-8') for x in data]
