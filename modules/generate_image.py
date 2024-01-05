
import pandas as pd
from collections import Counter
import ast
from openai import OpenAI
import urllib.request 
from PIL import Image 
import requests 
import os
from dotenv import load_dotenv

try:
    from . import retrieve_playlist
    from . import extract_data
except ImportError:
    import retrieve_playlist
    import extract_data

env_path = os.path.join(os.getcwd(), '.env')
load_dotenv(env_path)
OPENAI_KEY = os.getenv('OPENAI_API_KEY')
"""
# Spotify Playlist ID
playlist_id ="https://open.spotify.com/playlist/0O5sjTRPN1nORFjJNYfPyo?si=236a594d60e6463e"

"""

def create_prompt(playlist_id, input_user):
    """
    Function that takes the url of a spotify playlist and creates a prompt based on its' data 
    """
    analyzer = retrieve_playlist.SpotifyPlaylistAnalyzer(playlist_id)
    playlist_name, playlist_description, df = analyzer.retrieve_data()

    genres_string, artists_string, albums_string = extract_data.data_extractor(df)

    parameters = extract_data.get_mean_parameters(df)
    parameters_prompt = extract_data.parameters_prompt(parameters)

    prompt = f"""Create a colourful image with no text that visually represents the Spotify playlist titled '{playlist_name}'. 
        Emphasize themes and moods from the description of the playlist: '{playlist_description}', avoid adding text features to the image. 
        Incorporate elements or symbols related to the main genres of the playlist: {genres_string}, avoid adding text features to the image.. 
        In case the artists are well known, include abstract representations or iconic symbols associated with them; the artists are: {artists_string}, avoid adding text features to the image. 
        {parameters_prompt}.
        In addition, the user adds these intructions: {input_user}.
        Avoid using any text or words in the image and make sure that all the objects represented have the right proportions."""

    return playlist_name, prompt


def generate_image_with_dalle(prompt):
    """
    Function that, based on a prompt, generate an image with DALL-E 3
    """
    client = OpenAI(api_key=OPENAI_KEY)

    # Call the DALL-E API
    response = client.images.generate(model="dall-e-3",
    prompt=prompt,
    n=1,  # Number of images to generate
    size="1024x1024")
    
    return response.data[0].url

"""
# Example usage
PLAYLIST, PROMPT = create_prompt(playlist_id)
URL = generate_image_with_dalle(PROMPT)
print(URL)

data = requests.get(URL).content 
  
f = open(f'generated_images/z_{PLAYLIST}.jpg','wb') 
f.write(data) 
f.close() 
"""