# Spotify Image Generator

A flask webapp to generate images for Spotify playlists based on the playlist's url and a user input.

The data from the playlist is extracted from the Spotify API and merged to the user's input to create a prompt; ultimately the prompt is sent as a request to DALL-E 3 through the OpenAi API and the image is displayed on the page.

To use this app you must get yourself a *Spotify client id*, *Spotify secret key* and an *OpenAi key*, create a .env file and paste the keys as "OPENAI_API_KEY", "SPOTIFY_CLIENT" and "SPOTIFY_SECRET". 

With the current settings, generating one image costs about 4 cents.


Have fun experimenting!
