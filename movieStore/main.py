from bs4 import BeautifulSoup
from urllib import request
from movie import Movie
from movieRequisition import MovieRequisition
import atexit
import pickle
import os
import sys


def scrapMoviesFromImdb(movieList):
    with request.urlopen('https://www.imdb.com/chart/moviemeter') as response:
        soup = BeautifulSoup(response.read(), "html.parser")
    #f = open("scrapes/scrape.html","w+")
    # f.write(str(soup))
    # f.close()
    for tr in soup.select("tbody.lister-list tr"):
        # GET POSTER IMG
        td = tr.find('td', class_="posterColumn")
        urlPoster = td.find('img')['src']
        # String replace fix url poster size
        urlPoster = urlPoster.replace(
            '@._V1_UY67_CR0,0,45,67_AL_', '@._V1_UY0_CR0,0,0,0_AL_')

        # GET TITLE AND YEAR
        td = tr.find('td', class_="titleColumn")
        title = td.find('a').string
        # String replace year from (****) to ****
        year = td.find('span', class_="secondaryInfo").string
        year = year.replace('(', '')
        year = year.replace(')', '')

        # GET IMDB RATING
        td = tr.find('td', class_="ratingColumn imdbRating")
        rating = td.find('strong')
        if rating == None:
            rating = 0
        else:
            rating = rating.string

        movie = Movie(title, year, rating, urlPoster)
        movieList.append(movie)
    return movieList


def showMovies(movieList):
    for movie in movieList:
        if movie.requested == False:
            movie.tell()


def requestMovie(movieList, movieRequisitionList):
    print("What is the title of the film you which to request?")
    title = input()
    selectedMovie = None
    for movie in movieList:
        if movie.title == title:
            selectedMovie = movie
            break
    if(selectedMovie != None):
        selectedMovie.requested = True
        requesition = MovieRequisition(selectedMovie)
        movieRequisitionList.append(requesition)
        requesition.tell()
    return movieRequisitionList


def returnMovie(movieRequisitionList):
    print("What is the title of the film you which to return?")
    title = input()
    selectedReturn = None
    for request in movieRequisitionList:
        if request.movie.title == title and request.movie.requested == True:
            selectedReturn = request
            break
    if(selectedReturn != None):
        selectedReturn.movie.requested == False
        print("The movie {} was sucessfuly returned.".format(
            selectedReturn.movie.title))
    return movieRequisitionList


def pick(choice, movieList, movieRequisitionList):
    print("\n--------------------------------------------------------\n")
    if int(choice) == 1:
        showMovies(movieList)
    elif int(choice) == 2:
        requestMovie(movieList, movieRequisitionList)
    elif int(choice) == 3:
        returnMovie(movieRequisitionList)


def saveList(movieList, movieRequisitionList):
    print("Saving list")
    with open("scrapes/movieList", "wb") as mlTxt:
        pickle.dump(movieList, mlTxt)
    with open("scrapes/movieRequisitions", "wb") as mrTxt:
        pickle.dump(movieRequisitionList, mrTxt)


def main():
    movieList = []
    movieRequisitionList = []
    if os.path.isfile("scrapes/movieList") and os.path.getsize("scrapes/movieList") > 0:
        with open("scrapes/movieList", "rb") as mlTxt:
            print("Loading Movie List")
            movieList = pickle.load(mlTxt)
        with open("scrapes/movieRequisitions", "rb") as mrTxt:
            movieRequisitionList = pickle.load(mrTxt)
    else:
        scrapMoviesFromImdb(movieList)

    choice = 0
    while int(choice) < 4:
        print("\n--------------------------------------------------------\n")
        print("\nWhat do you want to do?\n1.Show movies \n2.Request a movie\n3.Return a movie\n4.Exit")
        choice = input()
        pick(choice, movieList, movieRequisitionList)
    saveList(movieList, movieRequisitionList)


if __name__ == "__main__":
    sys.setrecursionlimit(15000)
    main()
