from istorage import IStorage


class StorageCSV(IStorage):
    """
    Class for managing movies in csv file format.
    Implements methods for interacting with the movies database (db).
    """

    def __init__(self, file_path):
        self._file_path = file_path
        try:
            with open(file_path, 'r') as file:
                data_list = file.readlines()[1:]
        except FileNotFoundError:
            data_list = []

        movies = {}
        for movie in data_list:
            title, rating, year, poster = movie.split(',')
            movies[title] = {'rating': rating, 'release': int(year), 'poster': poster.strip()}
        self.movies = movies


    def list_movies(self):
        """ Getter function for movies """
        return self.movies.copy()


    def save_movies(self, new_movies):
        ''' writes the movies.json-file to the file '''

        with open(self._file_path, 'w') as file:
            for movie in new_movies:
                file.write(f"{movie},{new_movies[movie]['rating']},{new_movies[movie]['release']},{new_movies[movie]['poster']}\n")


    def add_movie(self, title, rating, year, poster=None):
        """
        Adds a movie to the movies db.
        Loads the information from the JSON file, add the movie,
        and saves it. The function doesn't need to validate the input.'
        """

        self.movies[title] = {'rating': rating, 'release': year, 'poster': poster}
        self.save_movies(self.movies)
        print(f"'{title}' added successfully to db!")


    def delete_movie(self, title):
        """
        Deletes a movie from the movies database.
        Loads the information from the JSON file, deletes the movie,
        and saves it. The function doesn't need to validate the input.
        """
        del self.movies[title]
        self.save_movies(self.movies)


    def update_movie(self, title, rating):
        """
        Updates a movie from the movies database.
        Loads the information from the JSON file, updates the movie,
        and saves it. The function doesn't need to validate the input.
        """
        self.movies[title].update({'rating': rating})
        self.save_movies(self.movies)
