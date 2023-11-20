import requests
import pika


def get_movie_composer(movie_name):
    api_key = "2197ec9acd132a70782fa27551abe546"
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}"

    search_response = requests.get(search_url)

    if search_response.status_code == 200:
        data = search_response.json()
        if data['results']:
            movie_id = data['results'][0]['id']
            credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}"
            credits_response = requests.get(credits_url)

            if credits_response.status_code == 200:
                credits_data = credits_response.json()
                composers = [member['name'] for member in credits_data['crew'] if
                             member['job'] == 'Music' or member['department'] == 'Sound']
                cast_crew_url = f"https://www.themoviedb.org/movie/{movie_id}/cast"
                composer_names = ', '.join(composers) if composers else "Composer not found"
                return composer_names, cast_crew_url
            else:
                return "Failed to retrieve movie credits."
        else:
            return "No movie found."
    else:
        return "Failed to search for the movie."


def callback(ch, method, properties, body):
    movie_name = body.decode()
    print(f"Received movie name: {movie_name}")
    composer_info, cast_crew_url = get_movie_composer(movie_name)

    message = f"Composer(s): {composer_info}\nCast & Crew Page: {cast_crew_url}"
    ch.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        body=message
    )


# Setting up RabbitMQ connection and consuming messages
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.queue_declare(queue='request-queue')

channel.basic_consume(queue='request-queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for movie names...')
channel.start_consuming()
