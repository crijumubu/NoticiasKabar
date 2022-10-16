class news:

    def __init__(self, newsTitle, newsDescription, newsCategory, newsUrl, newsDate, similarity):

        self.title = newsTitle
        self.description = newsDescription
        self.category = newsCategory
        self.url = newsUrl
        self.date = newsDate
        self.similarity = similarity

    def toString(self):

        return 'Title: ' + self.title + ', description: ' + self.description + ', category: ' + self.category + ', similarity: ' + str(self.similarity) + ', url: ' + self.url + ', crawl date: ' + self.date