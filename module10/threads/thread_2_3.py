import pprint

import requests

ACCESS_TOKEN = "5euZyGb1s2yiHmN59uQkGRkH2WUsIbdXNVhKnehXkWpYu_nNqxmsSQW0WU1qvL96"
RANDOM_GENRE_API_URL = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
GENIUS_API_URL = "https://api.genius.com/search"
GENIUS_URL = "https://genius.com"


genre = requests.get(RANDOM_GENRE_API_URL).json()

data = requests.get(GENIUS_API_URL, params={
                    "access_token": ACCESS_TOKEN, "q": genre}).json()

# pprint.pprint(data)

song_id = data["response"]["hits"][0]["result"]["api_path"]

print(f'{GENIUS_URL}{song_id}/apple_music_player')
