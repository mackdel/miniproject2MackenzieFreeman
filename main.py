# INF601 - Advanced Programming in Python
# Mackenzie Freeman
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt

# Grab the hotel data
hotels = pd.read_csv("hotels.csv", index_col=0)

# Remove the whitespaces in column headers
hotels.columns = hotels.columns.str.strip()

# Create Pet-Friendly column to indicate if hotel allows pets
hotels["Pet-Friendly"] = (
    hotels["HotelFacilities"].str.contains('Pets allowed', na=False) &
    ~hotels["HotelFacilities"].str.contains('NO Large pets allowed|NO Small pets allowed', na=False)
)

# Remove rows where HotelRating is All
hotels_filtered = hotels[hotels["HotelRating"] != "All"].copy()

# Rename star ratings
hotels_filtered.loc[:, 'HotelRating'] = hotels_filtered['HotelRating'].replace({
    'FiveStar': '5',
    'FourStar': '4',
    'ThreeStar': '3',
    'TwoStar': '2',
    'OneStar': '1'
})

# 1. Bar Chart: Amount of Pet-Friendly Hotels by Star Rating
grouped_counts = hotels_filtered[hotels_filtered["Pet-Friendly"]].groupby('HotelRating').size().reset_index(name='Count') # Count of Pet-Friendly hotels grouped by star rating
plt.bar(grouped_counts['HotelRating'], grouped_counts['Count'], color='r')
plt.title("Number of Pet-Friendly Hotels by Star Rating")
plt.xlabel("Star Rating")
plt.ylabel("Number of Pet-Friendly Hotels")
plt.show()

# 2. Pie Chart: Portion of Pet-Friendly and Non-Pet-Friendly Hotels
pet_friendly_counts = hotels_filtered['Pet-Friendly'].value_counts() # Count of both True and False values in Pet-Friendly
plt.pie(pet_friendly_counts, labels=['Non-Pet-Friendly', 'Pet-Friendly'], autopct='%1.2f%%', colors=['limegreen', 'turquoise'])
plt.title("Proportion of Pet-Friendly vs Non-Pet-Friendly Hotels")
plt.show()