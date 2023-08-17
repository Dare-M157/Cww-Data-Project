# Task 3

import pandas as pd
import matplotlib.pyplot as plt

# List of years from 2011 to 2020
years = list(range(2011, 2021))

# List of movie durations
durations = [103, 101, 99, 100, 100, 95,95, 96, 93, 90]

# Create a dictionary
movie_direct = {
    "years": years,
    "durations": durations
}

# Create a DataFrame
durations_df = pd.DataFrame(movie_direct)

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(durations_df['years'], durations_df['durations'], marker='o')
plt.title('Netflix Movie Durations 2011-2020')
plt.xlabel('Year')
plt.ylabel('Duration (minutes)')
plt.grid(True)
plt.show()