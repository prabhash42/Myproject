import requests

# TMDB API key
API_KEY = '2197ec9acd132a70782fa27551abe546'
BASE_URL = 'https://api.themoviedb.org/3'


def search_person():
    person_name = input("Enter the name of the actor/director: ")
    url = f"{BASE_URL}/search/person?api_key={API_KEY}&query={person_name}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get('results', [])
        if results:
            for index, person in enumerate(results, start=1):
                print(f"{index}. {person['name']}, Known for: {person['known_for_department']}")
            selection = int(input("Select the number of the person: ")) - 1
            if 0 <= selection < len(results):
                return results[selection]['id']
            else:
                print("Invalid selection.")
                return None
        else:
            print("No results found.")
            return None
    else:
        print("Failed to retrieve data.")
        return None


def get_person_filmography(person_id):
    url = f"{BASE_URL}/person/{person_id}/movie_credits?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        filmography = response.json()
        if 'cast' in filmography:
            print("\nActing Credits:")
            for movie in filmography['cast']:
                print(f"{movie['title']} - Character: {movie.get('character', 'N/A')}")
        if 'crew' in filmography:
            print("\nCrew Credits:")
            for movie in filmography['crew']:
                if movie['job'] == 'Director':
                    print(f"{movie['title']} - Director")
    else:
        print("Failed to get filmography.")


def show_top_rated_movies_by_year():
    year = input("Enter the year to get the top rated movies: ")
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&sort_by=vote_average.desc&year={year}"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json().get('results', [])
        print(f"\nTop rated movies for the year {year}:")
        for movie in movies[:10]:  # Get the top 10 movies
            print(f"{movie['title']} - Rating: {movie['vote_average']}")
    else:
        print("Failed to retrieve the top rated movies.")


def get_movie_details_by_title():
    title_query = input("Enter movie title to get details: ")
    search_url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={title_query}"
    response = requests.get(search_url)

    if response.status_code == 200:
        movies = response.json().get('results', [])
        if movies:
            print("Select a movie to get details:")
            for i, movie in enumerate(movies, 1):
                print(f"{i}. {movie['title']} ({movie.get('release_date', 'N/A')})")

            movie_choice = int(input("\nEnter the number of the movie: "))
            movie_id = movies[movie_choice - 1]['id']

            details_url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}"
            response = requests.get(details_url)
            if response.status_code == 200:
                movie_details = response.json()
                print(f"\nTitle: {movie_details['title']}")
                print(f"Overview: {movie_details['overview']}")
                print(f"Release Date: {movie_details['release_date']}")
            else:
                print("Failed to get movie details.")
        else:
            print("No movies found with that title.")
    else:
        print("Failed to search for movies.")
