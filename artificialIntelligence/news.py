class news:

    def __init__(self, newsTitle, newsDescription, newsUrl, newsDate, similarity):

        self.title = newsTitle
        self.description = newsDescription
        self.url = newsUrl
        self.date = newsDate
        self.similarity = similarity

    def toString(self):

        return 'Title: ' + self.title + ', description: ' + self.description + ', similarity: ' + str(self.similarity) + ', url: ' + self.url + ', crawl date: ' + self.date