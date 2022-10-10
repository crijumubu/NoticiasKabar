from cmath import cos
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from news import news
from connection import mongo

class artificalIntelligence:

    def __init__(self):

        self.getNews()
    
    def getNews(self):

        connection = mongo()
        data = connection.selectAll()

        return data

    def checkSimilarity(self, phrase):

        self.similarityVector = []
        phraseTokenization = word_tokenize(phrase.lower())

        for new in self.getNews():
            
            title = new['Title']
            description = new['Descripcion']
            url = new['Url']

            titleTokenization = word_tokenize(new['Title'].lower())
            titleCorrelation = self.wordSimilarity(phraseTokenization, titleTokenization)

            descriptionTokenization = word_tokenize(new['Descripcion'].lower())
            descriptionCorrelation = self.wordSimilarity(phraseTokenization, descriptionTokenization)

            if titleCorrelation > descriptionCorrelation:

                correlation = titleCorrelation
            else:

                correlation = descriptionCorrelation

            self.similarityVector.append(news(title, description, correlation, url)) # type: ignore

        self.topSimilarities()

    def wordSimilarity(self, phraseTokenization, newsWordTokenization):

        sw = stopwords.words('spanish') 

        l1 =[]
        l2 =[]

        phraseSet = {w for w in phraseTokenization if not w in sw}
        newsWordSet = {w for w in newsWordTokenization if not w in sw} 

        rvector = newsWordSet.union(phraseSet) 
        for w in rvector:
            if w in newsWordSet: l1.append(1)
            else: l1.append(0)
            if w in phraseSet: l2.append(1)
            else: l2.append(0)
        c = 0

        for i in range(len(rvector)):
            c+= l1[i]*l2[i]
        cosine = c / float((sum(l1)*sum(l2))**0.5)

        return cosine

    def topSimilarities(self):

        
        self.similarityVector.sort(key=lambda news: news.similarity, reverse = True)

        for i in range(0,10):
            
            print('\nNoticia ' + str(i+1) + ':\n\n\t' + self.similarityVector[i].toString() + '\n')
        

IAobject = artificalIntelligence();
IAobject.checkSimilarity('Colombia')