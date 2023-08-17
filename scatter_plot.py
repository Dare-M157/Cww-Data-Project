# Task 6

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file and create a DataFrame
csv_file_path = "netflix_data.csv"  # Update with the correct file path
netflix_df = pd.read_csv(csv_file_path)

# Subset only rows where the type is "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# Subset columns: title, country, genre, release year, duration
columns_to_keep = ['title', 'country', 'genre', 'release_year', 'duration']
netflix_df_movies_col_subset = netflix_df_movies_only[columns_to_keep]

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(netflix_df_movies_col_subset['release_year'], netflix_df_movies_col_subset['duration'], alpha=0.5)
plt.title('Movie Duration by Year of Release')
plt.xlabel('Release Year')
plt.ylabel('Movie Duration (minutes)')
plt.grid(True)
plt.show()
