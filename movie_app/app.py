import requests
import random
from statistics import median


class MovieApp:
    """
    MovieApp class. Contains storage, commands and menu for user interaction.
    """

    def __init__(self, storage):
        self._storage = storage


    def _command_list_movies(self):
        """ prints all movies.csv from the movies.csv-file (dict) """

        movies = self._storage.list_movies()
        print(f"{len(movies.keys())} Movies in total:")

        for movie, details in movies.items():
            title = movie
            rating = details['rating']
            release_year = details['release']
            print(f"{title} ({release_year}): {rating}")


    def _command_add_movie(self):
        """
        Fetches title, rating, release year and poster image from OMDb API
        Adds the movie to the csv storage file
        """

        movies = self._storage.list_movies()

        movie = str(input("Enter the new Movie: "))
        if movie in movies:
            print(f"{movie} already exists! Going back to Menu")
            return
        if not movie:
            print("Please enter a valid movie name. Going back to Menu.")
            return

        # Fetch data from OMDb API
        try:
            title, rating, release_year, poster_image_url = self._fetch_movie_data(movie)
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data from OMDb API. Check your internet connection. Details: {e}")
            return
        except KeyError:
            print(f"No data found for '{movie}' in OMDb. Please check the movie title and try again.")
            return
        except Exception as e:
            print(f"An unexpected error occurred while adding the movie: {e}")
            return

        # Add to storage
        try:
            self._storage.add_movie(title, rating, release_year, poster_image_url)
            print(f"{title} (Rating: {rating}, Released: {release_year}) was successfully added to the db.")

        except ValueError as v:
            print(f"Invalid input. Going back to Menu: {v}")
            return
        except Exception as e:
            print(f"An unexpected error occurred while adding the movie: {e}")
            return


    def _command_delete_movie(self):
        """ Deletes a movie from the csv file. """
        movies = self._storage.list_movies()
        movie = input("Enter the Movie you want to delete: ")
        if movie in movies:
            self._storage.delete_movie(movie)
            print(f"{movie} successfully deleted from the database.")
        else:
            print(f"{movie} not found in database. Going back to Menu.")


    def _command_update_movie(self):
        """ Updates a movie's rating in the csv file. """
        movies = self._storage.list_movies()
        movie = str(input("Enter the movie you want to update: "))
        if movie in movies:
            try:
                new_rating = float(input(f"Enter new rating for '{movie}' (0-10): "))
                if 0 <= new_rating <= 10:
                    self._storage.update_movie(movie, new_rating)
                    print(f"'{movie}' updated successfully with new rating: {new_rating}")
                else:
                    print("Rating must be between 0 and 10. Going back to Menu.")
            except ValueError as v:
                print("Invalid input. Going back to Menu", v)
        else:
            print(f"'{movie}' not found in the database. Try again!")


    def _command_movie_stats(self):
        """ Prints the median, average, best and worst movies from the Database. """

        print("Statistics in Movie Ratings:\n")
        movies = self._storage.list_movies()

        rating_list = []
        for title, details in movies.items():
            if details["rating"] != "N/A": # Skip unavailable ratings
                rating_list.append(float(details["rating"]))


        median_rating: float = round(median(rating_list), 2)
        average_rating = round(sum(rating_list) / len(rating_list), 2)
        max_rating = max(rating_list)
        min_rating = min(rating_list)
        best_movies = []
        worst_movies = []
        for title, details in movies.items():
            if details["rating"] != "N/A":
                if float(details["rating"]) == max_rating:
                    best_movies.append(title)
                if float(details["rating"]) == min_rating:
                    worst_movies.append(title)

        print(f"Median: {median_rating}")
        print(f"Average: {average_rating}")
        print(f"Best movies: {', '.join(best_movies)} - Rating: {max_rating}")
        print(f"Worst movies: {', '.join(worst_movies)} - Rating: {min_rating}")


    def _command_random_movie(self):
        """ picks a random movie from the movie dict. """

        movies = self._storage.list_movies()
        movie, details = random.choice(list(movies.items()))
        print(f"{movie} ({details["release"]}) was randomly picked. Rating: {details["rating"]}")


    def _command_search_movie(self):
        """ lets the user search for a movie by title or a part of the movie name. """

        movies = self._storage.list_movies()
        search = input("Enter the Movie Name (or a part of it) you are looking for: ")

        found_movies = []
        for movie, details in movies.items():
            if search.lower() in movie.lower():
                print(f"{movie} ({details["release"]} was found. Rating: {details["rating"]})")
                found_movies.append(movie)
        if not found_movies:
            print(f"No movies.csv found in the database for {search}.")


    def _command_sorted_movies(self):
        """ prints all movies.csv and their ratings in descending order by rating. """

        movies = self._storage.list_movies()

        sorted_movies = sorted(movies.items(),
                        key=lambda item: float(item[1]["rating"])
                        if item[1]["rating"] != "N/A" else float('-inf'), reverse=True)

        print("Movies by Ranking:")
        for movie, details in sorted_movies:
            print(f"{movie} ({details["release"]}): {details["rating"]}")


    def _fetch_movie_data(self, movie):
        """
        Loads movie details from OMDB.

        :param: movie: string name of movie
        :return: title, rating, year, poster_image_url
        """
        API_KEY = "9286827"
        search_q = "&t="
        URL = "https://www.omdbapi.com/?apikey=" + API_KEY + search_q

        movie_url = URL + movie
        res = requests.get(movie_url)
        data = res.json()

        title = data['Title']
        rating = data['imdbRating']
        year = data['Year']
        poster_image_url = data['Poster']

        return title, rating, year, poster_image_url


    def _generate_website(self):
        """
        Generates Website from template.
        Creates a new index.html file in the current directory, replacing placeholders with movie data.
        """

        movies = self._storage.list_movies()

        # read index_template
        with open("html_content/index_template.html", "r") as file:
            html_template = file.read()

        # generate content
        content = ""
        for title, details in movies.items():
            release_year = details['release']

            if 'poster' in details.keys() and details['poster'] != "N/A":
                poster = details['poster']
            else:
                poster = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"

            content += f"""
                <li>
                    <div class="movie">
                        <img class="movie-poster"
                             src="{poster}"/>
                        <div class="movie-title">{title}</div>
                        <div class="movie-year">{release_year}</div>
                    </div>
                </li>
            """

        # replace Placeholders
        placeholder = "__TEMPLATE_MOVIE_GRID__"
        html_content_new = html_template.replace(placeholder, content)

        # write new content to index.html
        with open("html_content/index.html", "w") as file:
            file.write(html_content_new)

        print("New website generated successfully!")


    def run(self):

        while True:
            func_dict = {
                '1': self._command_list_movies,
                '2': self._command_add_movie,
                '3': self._command_delete_movie,
                '4': self._command_update_movie,
                '5': self._command_movie_stats,
                '6': self._command_random_movie,
                '7': self._command_search_movie,
                '8': self._command_sorted_movies,
                '9': self._generate_website
                        }

            # Print menu
            print("---")
            print("Menu:")
            print(" 0 - Exit")
            print(" 1 - List Movies")
            print(" 2 - Add Movie")
            print(" 3 - Delete Movie")
            print(" 4 - Update Movie")
            print(" 5 - Statistics")
            print(" 6 - Random Movie")
            print(" 7 - Search for Movie")
            print(" 8 - Sorted Movies by Ranking")
            print(" 9 - Generate Website")
            print("---")

            # get user input and execute command
            command = str(input("Please enter your choice: "))

            if command == "0":
                print("See you next time.. Bye!")
                break
            elif command in func_dict:
                func_dict[command]()
                input("\nPress Enter to continue.")
            else:
                print("Invalid choice-number. Please try again.")
