import requests
from decouple import config

UNSPLASH_ACCESS_KEY = config('UNSPLASH')  # Replace with your Unsplash Access Key

def search_unsplash(query):
    url = "https://api.unsplash.com/search/photos"
    params = {
        'query': query,
        'client_id': UNSPLASH_ACCESS_KEY,
        'per_page': 5,  # Limit results to 5
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    return []