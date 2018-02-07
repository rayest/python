# coding=utf-8
import pymongo
from pymongo import MongoClient


def get_mongodb_version():
    print(pymongo.version)


def create_data():
    client = MongoClient('localhost', 27017)
    db = client.python
    collection = db.python
    collection.insert({"name": "mongodb教程2"})


if __name__ == '__main__':
    get_mongodb_version()
    create_data()
