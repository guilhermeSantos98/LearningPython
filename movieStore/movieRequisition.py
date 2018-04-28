from movie import Movie
import datetime


class MovieRequisition:
    def __init__(self, movie):
        self.movie = movie
        self.requestedAt = datetime.datetime.now()
        self.deliverAt = self.requestedAt+datetime.timedelta(days=5)

    def getMovieRequisition(self):
        return self

    def tell(self):
        print("{} was requested at {}, and needs to be delivered at {}\n".format(
            self.movie.title, self.requestedAt, self.deliverAt))
