import spacy
from news import news
from connection import mongo

class artificalIntelligence:

    def __init__(self):

        #self.nlp = spacy.load('es_dep_news_trf')
        self.nlp = spacy.load('es_core_news_sm')
        self.getNews()
        self.similarityVector = []
    
    def getNews(self):

        connection = mongo()
        data = connection.selectAll()

        return data

    def checkSimilarity(self, phrase):

        self.similarityVector = []

        nlpPhrase = self.nlp(phrase)

        for new in self.getNews():

            originalTitle = new['Title']
            originalDescription = new['Descripcion']
            originalUrl = new['Url']

            nlpTitle = self.nlp(originalTitle)
            nlpDescription = self.nlp(originalDescription)
            
            titleSimilarity = nlpTitle.similarity(nlpPhrase)
            descriptionSimilarity = nlpDescription.similarity(nlpPhrase)
            
            similarity = 0

            if titleSimilarity > descriptionSimilarity:

                similarity = titleSimilarity

            else:

                similarity = descriptionSimilarity

            self.similarityVector.append(news(originalTitle, originalDescription, similarity, originalUrl)) # type: ignore

        self.topSimilarities()

    def topSimilarities(self):

        self.similarityVector.sort(key=lambda news: news.similarity, reverse = True)

        for i in range(0,10):

            print('\nNoticia ' + str(i+1) + ':\n\n\t' + self.similarityVector[i].toString() + '\n')



IAobject = artificalIntelligence();
IAobject.checkSimilarity('Celular')