# Task 2

import pandas as pd

# List of years from 2011 to 2020
years = list(range(2011, 2021))

# List of movie durations
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# create a dictionary
movie_direct = {
      "years": years,
      "durations": durations
}

# Create a DataFrame
durations_df = pd.DataFrame(movie_direct)

# Print the entire DataFrame
print(durations_df)

