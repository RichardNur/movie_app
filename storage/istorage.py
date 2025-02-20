from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """
        Returns a dictionary of dictionaries containing movie information in the db.
        -- (The function loads the information from the JSON file and returns the data.) --
        e.g.: {"Pulp Fiction": {"rating": 8.3, "release": 1999}}
        """
        pass


    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """
        Adds a movie to the movies db.
        Loads the information from the JSON file, add the movie,
        and saves it. The function doesn't need to validate the input.
        """
        pass


    @abstractmethod
    def delete_movie(self, title):
        """
        Deletes a movie from the movies database.
        Loads the information from the JSON file, deletes the movie,
        and saves it. The function doesn't need to validate the input.
        """
        pass


    @abstractmethod
    def update_movie(self, title, rating):
        """
        Updates a movie from the movies db.
        Loads the information from the JSON file, updates the movie,
        and saves it. The function doesn't need to validate the input.
        """
        pass
