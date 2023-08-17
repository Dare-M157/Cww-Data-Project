# Task 4

import pandas as pd

# Read the CSV file and create a DataFrame
csv_file_path = "netflix_data.csv"  # Update with the correct file path
netflix_df = pd.read_csv(csv_file_path)

# Print the first five rows of the DataFrame
print(netflix_df.head())