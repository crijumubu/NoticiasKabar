from matplotlib.collections import Collection
from pymongo import MongoClient
from multipledispatch import dispatch

class mongo:

    def __init__(self):

        self.client = MongoClient('mongodb+srv://KabarDBA:KabarDBA312@cluster0.50a4eap.mongodb.net/retryWrites=true&w=majority')
        self.database = self.client.get_database('test')
        self.collection = self.database['modelnoticias']

    def insert(self, collection, many):

        if (many):

            self.collection.insert_many(collection)

        else:

            self.collection.insert_one(collection)

    @dispatch()
    def select(self):

        return list(self.collection.find())

    @dispatch(str)
    def select(self, title):

        return self.collection.find_one({'Title' : title})

    @dispatch()
    def delete(self):

        self.collection.delete_many({})

    @dispatch(str)
    def delete(self, title):

        self.collection.delete_one({'Title' : title})