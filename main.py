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

# Output only the Hotel Star Rating & Pet-Friendly columns
rating_pets = hotels[["HotelRating", "Pet-Friendly"]]

print(rating_pets.head())