# Task 8

import pandas as pd

# Read the CSV file and create a DataFrame
csv_file_path = "netflix_data.csv"  # Update with the correct file path
netflix_df = pd.read_csv(csv_file_path)

# Subset only rows where the type is "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# Subset columns: title, country, genre, release year, duration
columns_to_keep = ['title', 'country', 'release_year', 'duration', 'genre']
netflix_df_movies_col_subset = netflix_df_movies_only[columns_to_keep]

# Initialize an empty list to store colors
colors = []

# Use a loop to determine colors based on genre
for genre in netflix_df_movies_col_subset['genre']:
    if genre == "Children":
        colors.append("red")
    elif genre == "Documentaries":
        colors.append("blue")
    elif genre == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

# Print the first 10 values of the colors list
print(colors[:10])
