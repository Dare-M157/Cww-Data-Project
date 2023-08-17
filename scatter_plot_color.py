# Task 9

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file and create a DataFrame
csv_file_path = "netflix_data.csv"  # Update with the correct file path
netflix_df = pd.read_csv(csv_file_path)

# Subset only rows where the type is "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# Subset columns: title, country, genre, release year, duration
columns_to_keep = ['title', 'country', 'release_year', 'duration', 'genre']
netflix_df_movies_col_subset = netflix_df_movies_only[columns_to_keep]

# Initialize the colors list
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

# Create a scatter plot with colored points
plt.figure(figsize=(10, 6))
plt.scatter(netflix_df_movies_col_subset['release_year'], netflix_df_movies_col_subset['duration'], c=colors, alpha=0.5)
plt.title('Movie Duration by Year of Release')
plt.xlabel('Release Year')
plt.ylabel('Movie Duration (minutes)')
plt.grid(True)
plt.show()

# Task 10

# Are we certain that movies are getting shorter?
# Having visualized and analyzed the Netflix movie data, one can observe trends in movie durations over the years and identify differences among genres, however the scatter plots alone might not provide definitive evidence of a consistent trend of movies getting shorter. Further analysis could provide more insights into  a significant change in movie lengths over time

