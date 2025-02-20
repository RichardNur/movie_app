from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCSV


def main():
    """
    A command-line application for managing a movie database.

    This app allows users to list, add, update, and delete movies stored in a JSON file.
    Users can interact with the database using a simple text-based menu.
    """

    # csv:
    # storage = StorageCSV('movies.csv')
    # movie_app = MovieApp(storage)
    # movie_app.run()

    # json:
    storage = StorageJson('movies.json')
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
