import requests
import re
import time
import tqdm
from bs4 import BeautifulSoup

# Genius API access token and base URL
API_TOKEN = "pDiwG885oOi3MPIis2AREt1w_51coNtdwQDZtKY8QvTaWjxdya0PtxYZSv8-7iOY"
GENIUS_URL = "https://api.genius.com"

def search_genius(query):
    """
    Search the Genius API for songs, artists, or albums.
    """
    endpoint = f"{GENIUS_URL}/search"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    params = {
        "q": query  # The search term
    }
    
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()  # Raise HTTP errors if any
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error searching Genius API: {e}")
        return None
    
def get_lyrics(song_id):
    """
    Fetch the lyrics info for a specific song by ID.
    """
    endpoint = f"{GENIUS_URL}/songs/{song_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # Raise HTTP errors if any
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching lyrics: {e}")
        return None
    
def find_lyrics(url):
    """
    Extract lyrics from a Genius URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTP errors if any
        soup = BeautifulSoup(response.text, "html.parser")
        lyrics = "\n".join([element.get_text(separator="\n") for element in soup.find_all('div', {'data-lyrics-container': 'true'})])
        # Delete the indications in [] and ()
        lyrics = re.sub(r"[\(\[].*?[\)\]]", "", lyrics, flags=re.DOTALL)
        return lyrics
    except requests.exceptions.RequestException as e:
        print(f"Error fetching lyrics: {e}")
        return None
    
def fetch_lyrics(dataframe):
    # Create a new dataframe to store the lyrics and keep the original intact
    new_dataframe = dataframe.copy()
    for song_name in tqdm.tqdm(new_dataframe['Song']):
        # Search for the song
        search_results = search_genius(song_name)
        
        # Check if the search was successful
        if search_results:
            # Get the first search result
            search_hits = search_results.get("response", {}).get("hits")
            if search_hits:
                search_hit = search_hits[0]
                
                # Get the song URL
                song_url = search_hit.get("result", {}).get("url")
                
                # Get the song lyrics
                lyrics = find_lyrics(song_url)
                
                # Store the song lyrics
                new_dataframe.loc[new_dataframe['Song'] == song_name, 'Lyrics'] = lyrics
                
                time.sleep(0.5)  # Be polite to the API
                
    return new_dataframe