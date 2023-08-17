# Task 1

# List of years from 2011 to 2020
years = list(range(2011, 2020))

# List of movie durations
durations = [103, 101, 99, 100, 100, 95, 96, 93, 90]

# create a dictionary
movie_direct = {
      "years": years,
      "durations": durations
}

# Calculate the average duration
average_duration = sum(durations) / len(durations)

# Print the dictionary and average duration
print("Movie Dictionary:", movie_direct)
print(f"Average Duration: {average_duration} minutes")

# Inspect the dictionary contents
print("Years:", movie_direct["years"])
print("Durations:", movie_direct["durations"])



import pandas as pd

years = list(range(2011, 2020))
durations = [103, 101, 99, 100, 100, 95, 96, 93, 90]  #  one element is missing
# Adding a placeholder duration value for the missing year
durations.append(None)

# Create DataFrame
durations_df = pd.DataFrame(movie_direct)
print(movie_direct)







