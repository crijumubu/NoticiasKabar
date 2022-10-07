from connection import mongo
import json

class controller:

    def __init__(self):
        
        self.mongo = mongo()
        self.getJson()

    def getJson(self):

        path = './../news/news.json'

        with open(path) as news:

            self.newsCollection = json.load(news)
    
    def countElements(self):

        return len(self.mongo.select())

    def insert(self):

        self.mongo.insert(self.newsCollection)

    def insertWithoutRepeating(self):
        
        for news in self.newsCollection:

            newsTitle = news['Title']

            if (self.mongo.select(newsTitle) == None):

                self.mongo.insert(news, False)

    def close(self):

        self.mongo.client.close()

control = controller()
control.insertWithoutRepeating()
control.close()