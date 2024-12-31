import requests

UNSPLASH_ACCESS_KEY = 't05cL0A2qAk-TQkfzjhHCG9xUdqDJzKo8FU7h6zMqaE'  # Replace with your Unsplash Access Key

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