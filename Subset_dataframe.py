# Task 5

import pandas as pd

# Read the CSV file and create a DataFrame
csv_file_path = "netflix_data.csv"  # Update with the correct file path
netflix_df = pd.read_csv(csv_file_path)

# Subset only rows where the type is "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# Subset columns: title, country, genre, release year, duration
columns_to_keep = ['title', 'country', 'genre', 'release_year', 'duration']
netflix_df_movies_col_subset = netflix_df_movies_only[columns_to_keep]

# Print the first five rows of the subset DataFrame
print(netflix_df_movies_col_subset.head())
