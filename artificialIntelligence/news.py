class news:

    def __init__(self, newsTitle, newsDescription, similarity, newsUrl):

        self.title = newsTitle
        self.description = newsDescription
        self.url = newsUrl

        self.similarity = similarity

    def toString(self):

        return 'Title: ' + self.title + ', description: ' + self.description + ', similarity: ' + str(self.similarity) + ', url: ' + self.url