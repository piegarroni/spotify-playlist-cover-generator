import ast
from collections import Counter


def get_mean_parameters(df):
    """
    Function to convert high and low playlist's parameters into a string to add to the prompt
    """
    parameters = {'energy': df['energy'].mean(), 'danceability': df['danceability'].mean(), 'speechiness': df['speechiness'].mean(), 'acousticness': df['acousticness'].mean(), 'valence': df['valence'].mean()}
    return parameters


def find_top_5_genres(df, column_name):
    """
    Return a list of the 5 most common genres in the playlist
    """
    # Flatten the list of lists into a single list
    all_strings = [item for sublist in df[column_name] for item in sublist]
    
    # Count the frequency of each string
    string_counts = Counter(all_strings)

    # Find the 5 most common strings
    top_5 = string_counts.most_common(5)

    return [word for word, count in top_5]


def find_top_5_words(df, column_name):
    """
    Return a list of teh 5 most common words contained in the genres in the playlist
    """
    # Flatten the list of lists and split each string into words
    all_words = [word for sublist in df[column_name] for string in sublist for word in string.split()]

    # Count the frequency of each word
    word_counts = Counter(all_words)

    # Find the 5 most common words
    top_5 = word_counts.most_common(5)
    return [word for word, count in top_5]


def find_top_5_artist(df, column_name):
    """
    Return the 5 most common artists/albums
    """
    # Flatten the list of lists and split each string into words
    all_words = [artist for artist in df[column_name]]

    # Count the frequency of each word
    word_counts = Counter(all_words)

    # Find the 5 most common words
    top_5 = word_counts.most_common(5)

    return [word for word, count in top_5]



def data_extractor(df):
    """
    Function to extract top genres, artists, albums from the previous function, convert them to string and return them    
    """
    # Call the function with your DataFrame and column name
    genres = find_top_5_genres(df, 'genres')
    genres_words = find_top_5_words(df, 'genres')

    # merge genres
    genres = genres + genres_words
    genres_string = ', '.join(genres)

    # Call the function with your DataFrame and column name
    artist_names = find_top_5_artist(df, 'artist_name')
    # artist strings
    artists_string = ', '.join(artist_names)


    # Call the function with your DataFrame and column name
    album_names = find_top_5_artist(df, 'album_name')
    # album strings
    albums_string = ', '.join(album_names)


    return genres_string, artists_string, albums_string




def parameters_prompt(parameters):
    """
    Function to convert the high or low average parameters into text to add to the prompt
    """
    # Filter parameters based on the specified thresholds
    significant_params = {param: value for param, value in parameters.items() if value > 0.7 or value < 0.3}

    # Create descriptions for each significant parameter
    param_descriptions = []
    for param, value in significant_params.items():
        if value > 0.7:
            param_descriptions.append(f"very high {param}")
        elif value < 0.3:
            param_descriptions.append(f"very low {param}")

    # Combine the parameter descriptions into the prompt
    param_str = ", ".join(param_descriptions)
    if param_str:
        param_str = f"The image should reflect the music's characteristics, such as: {param_str}, "

    return param_str.rstrip(", ")


"""
# Example parameters
example_parameters = {
    'energy': 0.8,        # High
    'danceability': 0.5,  # Not significant
    'speechiness': 0.2,   # Low
    'acousticness': 0.9,  # High
    'valence': 0.3        # Not significant
}

# Generating the prompt with the new function
#prompt_parameters = parameters_prompt(example_parameters)

"""