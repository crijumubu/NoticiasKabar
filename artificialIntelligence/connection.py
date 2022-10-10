from pymongo import MongoClient
from credentials import credentials

class mongo:

    def __init__(self):

        self.credential = credentials()
        self.client = MongoClient(self.credential.getCrendential())
        self.database = self.client.get_database('test')
        self.collection = self.database['modelnoticias']

    def insert(self, collection, many):

        if (many):

            self.collection.insert_many(collection)

        else:

            self.collection.insert_one(collection)

    def selectAll(self):

        return list(self.collection.find())

    def selectEspecific(self, title):

        return self.collection.find_one({'Title' : title})

    def deleteAll(self):

        self.collection.delete_many({})

    def deleteEspecific(self, title):

        self.collection.delete_one({'Title' : title})