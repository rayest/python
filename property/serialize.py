import json


class Asset(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__)


if __name__ == '__main__':
    a = Asset('lee', 100.80)
    print(a.serialize())
