# 🎬 MovieApp - Your Personal Movie Database Manager!

The **MovieApp** is a Python-based application that allows users to manage their own movie database right from the command line! Whether you want to add, delete, search, or fetch ratings for your favorite movies, this app has got you covered.

---

## ✨ Features

1. Maintain your personal Movie Database
2. View the Movies and Details in the web Browser, using index.html

- **Add Movies**: Add a movie to your database with details fetched from the OMDb API.
- **List Movies**: View all movies in your collection along with their ratings and release years.
- **Delete Movies**: Remove movies that you no longer want in your database.
- **Update Movie Ratings**: Update the rating for a movie in your collection.
- **Statistics**: Get insights into your movie collection:
  - Median Rating
  - Average Rating
  - Best Movie(s)
  - Worst Movie(s)
- **Search Movies**: Search your database by title or partial name.
- **Random Movie Selection**: Let the app randomly suggest a movie from your list.
- **Sort Movies**: Display all movies sorted by rating in descending order.

---

## 🛠️ Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-repo/movie_app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd movie_app
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

1. Start the application by running:
   ```bash
   python movie_app.py
   ```
2. Interact with the application through the menu:
   - Choose an option from the displayed menu to manage your movie database.

---

## 🗂️ Main Commands

| Command                        | Description                                                                     |
|--------------------------------|---------------------------------------------------------------------------------|
| `List Movies`                  | Displays all movies in your database with details like ratings and release year.|
| `Add Movie`                    | Add a new movie by providing its title. Data is fetched from the OMDb API.      |
| `Update Movie`                 | Update the rating for an existing movie.                                        |
| `Delete Movie`                 | Remove a movie from your database.                                              |
| `Statistics`                   | Provides median, average, best, and worst-rated movies.                         |
| `Search for Movie`             | Search the database for movies based on the title or a part of the title.       |
| `Random Movie Suggestion`      | Picks a random movie from the database.                                         |
| `Sorted Movies by Rating`      | Displays movies sorted by their rating (highest first).                         |
| `Exit`                         | Exits the application.                                                          |

---

## 🧰 Technologies Used

- **Language**: Python 3.12+
- **Dependencies**:
  - `requests` - To fetch movie details from the OMDb API.
  - `random` - For random movie selection.
  - `statistics` - For calculating median rating.
  - Custom local storage (supports functions like `add_movie`, `delete_movie`, etc.).

---

## 🌐 API Integration

The **MovieApp** integrates with the OMDb API to fetch movie details (like rating, release year, and poster).

- **API URL**: `https://www.omdbapi.com/`
- **Key**: Make sure you have a valid API Key integrated within the `_fetch_movie_data` method.

For more information, visit [OMDb API Official Website](https://www.omdbapi.com/).

---

## 🎯 Future Enhancements

We plan to extend the features of MovieApp with the following updates:
- 🌍 **Web Interface**: Build a fancy web frontend for better user interactions.
- 📊 **Enhanced Statistics**: Add more insights like genre-based rating, actor appearances, etc.
- 📂 **Export Data**: Option to export movie data in CSV, JSON, or HTML formats.
- 🖼️ **Poster Display**: View movie posters directly in the app or via a web interface.

---

## 🚧 Known Limitations

- The app currently relies solely on OMDb API for fetching data. If the API goes down or returns incomplete data, certain features might not work as expected.
- No persistent storage implementation for movie posters (URLs are provided but not downloaded).

---

## 🏗️ Contribution

We welcome contributions from the community! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch with your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push the changes:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Submit a pull request 🚀!

---

Enjoy managing your movie collection with ✨ **MovieApp**!
