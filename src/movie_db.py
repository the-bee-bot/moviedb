"""
Movie database - bunch of movie objects
"""
from media import Movie
import fresh_tomato
import pickle
import os
import sys


class MovieDb:
    DBNAME = os.path.join(".", "movies.db")

    def __init__(self):
        """
        Init the movie database with default options
        Returns: None
        """
        # dictionary to hold movie objects against their titles
        self.movies = {}

        try:
            if os.path.exists(self.DBNAME):
                # this means save option is enabled and a movie database is found. Load objects from that to list.
                with open(self.DBNAME, "rb") as db:
                    movies_dict_from_db = pickle.load(db)
                    if type(movies_dict_from_db) == dict:
                        for movieTitle in movies_dict_from_db:
                            # getting the movie object from the dictionary
                            movieObj = movies_dict_from_db[movieTitle]
                            # check the movie object and add it to the movies dict
                            if type(movieObj) == Movie: self.movies[movieTitle] = movieObj
                    else:
                        raise Exception("DB Corrupted")

        except Exception as ex:
            # remove db if anything wrong happens while loading from db
            if os.path.exists(self.DBNAME): os.remove(self.DBNAME)
        finally:
            self.load_default_movies()

    def load_default_movies(self):
        """
        Creates movie objects and adds to the movies list.
        Returns: None
        """

        self.movies["Uriyadi"] = (Movie("Uriyadi",
                                        "A political thriller set in the late 1990s, revolving around an engineering college in the interiors of Tamil Nadu",
                                        "https://upload.wikimedia.org/wikipedia/commons/f/f0/Uriyadi_Tamil_Movie.jpg",
                                        "https://www.youtube.com/watch?v=hifdGU654R4"))

        self.movies["Iraivi"] = (Movie("Iraivi",
                                       "Three women become liberated after unfortunate circumstances drive their husbands to become involved in crime.",
                                       "https://upload.wikimedia.org/wikipedia/en/3/36/Iraivi.jpg",
                                       "https://www.youtube.com/watch?v=DH3iKNTT9-M"))

        self.movies["Kabali"] = (Movie("Kabali",
                                       "An aged gangster tries to protect his family and his business from his enemies.",
                                       "https://upload.wikimedia.org/wikipedia/en/9/9e/Rajinikanth_in_Kabali.jpg",
                                       "https://www.youtube.com/watch?v=9mdJV5-eias"))

        self.movies["Virumandi"] = (Movie("Virumandi",
                                          "A reporter researching the death penalty meets Virumandi and Kuthala. While listening to their versions of the same story, she realises that Virumandi is being punished for a crime he did not commit.",
                                          "https://upload.wikimedia.org/wikipedia/en/thumb/7/75/Virumaandi.jpg/220px-Virumaandi.jpg",
                                          "https://www.youtube.com/watch?v=fLhW-oYtd4Q"))

    def save_movie_dict(self):
        # persists the movies_dict class variable using pickle
        with open(self.DBNAME, "wb") as db:
            pickle.dump(self.movies, db)

    def movie_db_exists(self):
        """
        returns if db file exists or not
        Returns (bool): bool value
        """
        return os.path.exists(self.DBNAME)

    def get_movies_as_list(self):
        """
        Returns (obj:list of obj:Movie) : list of movie objects sorted by their titles
        """
        return [self.movies[title] for title in sorted(self.movies.keys())]

    def delete_db(self):
        # delete db file
        if self.movie_db_exists(): os.remove(self.DBNAME)


MMDB = MovieDb()


def main():
    if type(sys.argv) and len(sys.argv) > 1:
        # an option is given
        option = sys.argv[1].strip()
        if option == "-sw":
            # switches database option. If enabled then creates a db file. Else deletes if any exists.
            if MMDB.movie_db_exists():
                # if already exists disable db options.
                delete = input(
                    "DB option is enabled (All the movies added will be lost). "
                    "Do you want to disable it and hence delete the db file? Press Y/N")
                if delete.lower().startswith("y"):
                    #         user wants to continue to delete db
                    MMDB.delete_db()
            else:
                # enable db options.
                MMDB.save_movie_dict()
        elif option == "-a":
            print("Interactive mode!!! add your favourite movie to MMDB.")
            while True:
                title = input("Movie title: ")
                story = input("Story line: ")
                poster = input("URL to poster image: ")
                trailer = input("URL to youtube trailer: ")
                MMDB.movies[title] = Movie(title, story, poster, trailer)
                more = input("%s is added to MMDB. Do you want to add more? Press Y/N " % (title))
                if more.lower().startswith("n"): break
            MMDB.save_movie_dict()
        #
        # elif option == "-e":
        #     # fixme have to add edit option
        #     print("Interactive mode!!! edit your favourite movie in the MMDB.")
        elif option == "-d":
            print("Interactive mode!!! delete your favourite movie from MMDB.")
            while True:
                print("ID: Movie Title")
                movie_titles = sorted(MMDB.movies.keys())
                for idx, title in enumerate(movie_titles):
                    print("%s : %s " % (idx + 1, title))
                # id of the movie to delete
                idx = eval(input("Enter the id of the movie that you want to delete: "))
                if type(idx) == int and idx <= len(MMDB.movies):
                    MMDB.movies.pop(movie_titles[idx - 1])
                    more = input(
                        "%s is deleted from MMDB. Do you want to delete more? Press Y/N " % (movie_titles[idx - 1]))
                    # exit interactive mode
                    if more.lower().startswith("n"): break

    # generate html code and display that to user.
    fresh_tomato.open_movies_page(MMDB.get_movies_as_list())


if __name__ == '__main__':
    main()
