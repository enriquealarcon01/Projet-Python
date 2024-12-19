import requests
import pandas as pd
import tqdm
import time

# MusicBrainz API base URL
BASE_URL = "https://musicbrainz.org/ws/2"

def fetch_artist_data(all_artists):
    df_artists = pd.DataFrame(columns=['Artist', 'Country', 'Type', 'Gender', 'Rating', 'Tags'])
    for index, artist_name in tqdm.tqdm(enumerate(all_artists), total=len(all_artists)):
        
        # Fetch artist data
        artists = get_artist_list(artist_name)
            
        # Search for data of the first artist
        if artists:
            artist = artists[0]
            
            artist_name = artist.get("name")
            artist_type = artist.get("type")
            artist_country = artist.get("country")
            
            artist_id = artist.get("id")
            if artist_id:
                artist_data = get_artist_info(artist_id)
                if artist_data:
                    
                    gender = artist_data.get("gender")
                    rating = artist_data.get("rating")
                    tags = artist_data.get("tags")
                    
                    df_artists.loc[index] = [artist_name, artist_country, artist_type, gender, rating, tags]
                                
                else:
                    print("No artist data found.")
            else:
                print("No artist ID found.")
        else:
            print("No artist information found.")
            
        time.sleep(1)  # Be polite to the API
        
    return df_artists

def get_artist_list(artist_name):
    """
    Fetch artist information from the MusicBrainz API.
    """
    endpoint = f"{BASE_URL}/artist"
    params = {
        "query": artist_name,  # Search for the artist by name
        "fmt": "json"         # Request JSON response
    }
    
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data["artists"] if "artists" in data else None
    except requests.exceptions.RequestException as e:
        return None
    
def get_artist_info(artist_id):
    """
    Fetch detailed information for a specific artist by ID.
    """
    endpoint = f"{BASE_URL}/artist/{artist_id}"
    params = {
        "inc": "aliases+tags+ratings",  # Include additional information
        "fmt": "json"                   # Request JSON response
    }
    
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        return None