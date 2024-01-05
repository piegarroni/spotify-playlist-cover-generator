# Spotify Image Generator

## What it is 
A Flask webapp to generate images for Spotify playlists based on the playlist's url and a user input.

## How it works
The data from the playlist is extracted from the Spotify API and merged to the user's input to create a prompt; ultimately the prompt is sent as a request to DALL-E 3 through the OpenAi API and the image is displayed on the page.

The input page looks something like this:
<br>
<br>
<p align="center">
  <img src="/images/index2.png" width=90%>
</p>
<br>
<br>

## Some images generated from my playlists

<h3 align="center">Playlist name: Bob Would Like This</h3>

<p align="center">
  <img src="/images/Bob%20would%20like%20this.jpg" width="600">
</p>
This playlist is a mix of raggae and dub music (Bob Marley, Mo'kalamity...)
<br>

<h3 align="center">Playlist name: Chill but Psychedelic</h3>

<p align="center">
  <img src="/images/z_Chill%20but%20Psychedelic.jpg" width="600">
</p>
This playlist is a collection of chill songs characterized psychedelic sounds (Pink Floyd, psy electronic music...)
<br>

<h3 align="center">Playlist name: Amazing Guitars</h3>

<p align="center">
  <img src="/images/z_Amazing%20Guitars.jpg" width="600">
</p>
This playlist is a blend of songs whose sound is composed mostly by guitars (flamenco, rock guitar solos...)
<br>
<br>

## How To Use

To use this app you must get yourself a *Spotify client id*, *Spotify secret key* and an *OpenAi key*, create a .env file and paste the keys as "OPENAI_API_KEY", "SPOTIFY_CLIENT" and "SPOTIFY_SECRET". 

With the current settings, generating one image costs about 4 cents.

I recommend adding a description to your playlists for better results, doesn't have to be too specific.

# Have fun experimenting!


