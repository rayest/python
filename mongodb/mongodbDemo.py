# coding=utf-8
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)


def get_mongodb_version():
    print(pymongo.version)


def create_data():
    db = client.python
    collection = db.python
    collection.insert({"name": "JAVA"})
    collection.insert({"name": "REDIS"})
    print(collection.find_one({"name": "JAVA"}))


if __name__ == '__main__':
    get_mongodb_version()
    create_data()
