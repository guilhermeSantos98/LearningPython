class Movie:
    def __init__(self, title, year, imdb, duration):
        self.title = title
        self.year = year
        self.imdb = imdb
        self.duration = duration
        self.requested = False

    def getMovie(self):
        return self

    def tell(self):
        if self.requested == True:
            print("{} was released in {}, has a rating of {}, and a total duration of {} minutes, and is already requested\n".format(
                self.title, self.year, self.imdb, self.duration))
        else:
            print("{} was released in {}, has a rating of {}, and a total duration of {} minutes, and isn't requested\n".format(
                self.title, self.year, self.imdb, self.duration))
