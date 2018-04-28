from movie import Movie
from movieRequisition import MovieRequisition
listMovie = []
listMovieRequisition = []


def addMovie():
    print("What is the title of the movie?")
    title = input()
    print("What is the year of release of {}?".format(title))
    year = input()
    print("What is the imdb rating of {}?".format(title))
    imdb = input()
    print("What is the total duration of {} in minutes?".format(title))
    duration = input()
    mov = Movie(title, year, imdb, duration)
    listMovie.append(mov)


def showMovies():
    for movie in listMovie:
        if movie.requested == False:
            movie.tell()


def requestMovie():
    print("What is the title of the film you which to request?")
    title = input()
    selectedMovie = None
    for movie in listMovie:
        if movie.title == title:
            selectedMovie = movie
            break
    if(selectedMovie != None):
        selectedMovie.requested = True
        requesition = MovieRequisition(selectedMovie)
        listMovieRequisition.append(requesition)
        requesition.tell()


def returnMovie():
    print("What is the title of the film you which to return?")
    title = input()
    selectedReturn = None
    for request in listMovieRequisition:
        if request.movie.title == title and request.movie.requested == True:
            selectedReturn = request
            break
    if(selectedReturn != None):
        selectedReturn.movie.requested == False
        print("The movie {} was sucessfuly returned.".format(
            selectedReturn.movie.title))


def pick(choice):
    print("\n--------------------------------------------------------\n")
    if int(choice) == 1:
        addMovie()
    elif int(choice) == 2:
        showMovies()
    elif int(choice) == 3:
        requestMovie()
    elif int(choice) == 4:
        returnMovie()
    elif int(choice) == 5:
        quit()


choice = 0
while choice != -1:
    print("\n--------------------------------------------------------\n")
    print("\nWhat do you want to do?\n1.Add movie \n2.Show all the movies\n3.Request a movie\n4.Return a movie\n5.Exit")
    choice = input()
    pick(choice)
