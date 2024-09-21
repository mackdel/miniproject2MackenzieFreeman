# INF601 - Advanced Programming in Python
# Mackenzie Freeman
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt

# Grab the hotel data
hotels = pd.read_csv("hotels.csv", index_col=0)

# Remove the whitespaces in column headers
hotels.columns = hotels.columns.str.strip()

# Get the Hotel Star Rating & Facilities
rating_facilities = hotels[["HotelRating", "HotelFacilities"]]

print(rating_facilities.head())