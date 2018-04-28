class Movie:
    def __init__(self, title, year, imdb,urlPoster):
        self.title = title
        self.year = year
        self.imdb = imdb
        self.urlPoster = urlPoster
        self.requested = False

    def getMovie(self):
        return self

    def tell(self):
        if self.requested == True:
            print("{} was released in {}, has a rating of {}, and is already requested\n".format(
                self.title, self.year, self.imdb))
        else:
            print("{} was released in {}, has a rating of {}, and isn't requested\n".format(
                self.title, self.year, self.imdb))
