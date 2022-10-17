from pymongo import MongoClient
from credentials import credentials
from bson.json_util import dumps

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

    def selectEspecificByTitle(self, title):

        return self.collection.find_one({'Title' : title})

    def selectEspecificByCategory(self, category):

        return list(self.collection.find({'Category' : category}))

    def updateEspecific(self, title, category):

        self.collection.update_one({'Title' : title}, {'$set' : {'Category' : category}})
    
    def updateAll(self):

        self.collection.update_many({}, {'$set' : {'Category' : ''}})

    def deleteAll(self):

        self.collection.delete_many({})

    def deleteEspecific(self, title):

        self.collection.delete_one({'Title' : title})

    def deleteBySource(self, source):

        self.collection.delete_many({'Source' : source})

    def extractJson(self):

        cursor = self.selectAll()
        with open('news.json', 'w') as file:
            file.write('[')
            for i in range (0, len(cursor)):
                file.write(dumps(cursor[i]))
                if (i + 1 != len(cursor)):
                    file.write(',\n')
            file.write(']')