# INF601 - Advanced Programming in Python
# Mackenzie Freeman
# Mini Project 2

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Make charts folder if there is not one already
os.makedirs("charts", exist_ok=True)

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
plt.bar(grouped_counts['HotelRating'], grouped_counts['Count'], color='blue')
plt.title("Number of Pet-Friendly Hotels by Star Rating")
plt.xlabel("Star Rating")
plt.ylabel("Number of Pet-Friendly Hotels")
plt.savefig("charts/BarChart.png")

# 2. Pie Chart: Portion of Pet-Friendly and Non-Pet-Friendly Hotels
pet_friendly_counts = hotels_filtered['Pet-Friendly'].value_counts() # Count of both True and False values in Pet-Friendly
plt.pie(pet_friendly_counts, labels=['Non-Pet-Friendly', 'Pet-Friendly'], autopct='%1.2f%%', colors=['limegreen', 'turquoise'])
plt.title("Proportion of Pet-Friendly vs Non-Pet-Friendly Hotels")
plt.savefig("charts/PieChart.png")

# 3. Stacked Bar Chart: Pet-Friendly vs. Non-Pet-Friendly Hotels by Star Rating
stacked_grouped_counts = hotels_filtered.groupby(['HotelRating', 'Pet-Friendly']).size().unstack(fill_value=0) # Count of both True and False values in Pet-Friendly grouped by star rating
stacked_grouped_counts.plot(kind='bar', stacked=True, color=['darkorange', 'darkred'])
plt.title("Pet-Friendly vs Non-Pet-Friendly Hotels by Star Rating")
plt.xlabel("Star Rating")
plt.ylabel("Number of Hotels")
plt.legend(["Non-Pet-Friendly", "Pet-Friendly"])
plt.savefig("charts/StackedBarChart.png")

# 4. Heatmap: Pet-Friendliess by Hotel Star Rating
heatmap_data = hotels_filtered.pivot_table(index='HotelRating', columns='Pet-Friendly', aggfunc='size', fill_value=0) # Reshape data into matrix
sns.heatmap(heatmap_data, annot=True, cmap="RdPu", fmt="d") # Shows data values in each cell
plt.title("Pet-Friendliness by Hotel Star Rating")
plt.xlabel("Pet-Friendly")
plt.ylabel("Star Rating")
plt.savefig("charts/Heatmap.png")

# 5. 100% Stacked Bar Chart: Pet-Friendly vs. Non-Pet-Friendly Hotels per Star Rating
stacked_grouped_counts = stacked_grouped_counts.div(stacked_grouped_counts.sum(axis=1), axis=0) * 100 # Calculate the percentages
stacked_grouped_counts.plot(kind='bar', stacked=True, color=['orange', 'green'])
plt.title("Pet-Friendly vs Non-Pet-Friendly per Star Rating")
plt.xlabel("Star Rating")
plt.ylabel("% of Hotels")
plt.legend(["Non-Pet-Friendly", "Pet-Friendly"], loc='lower right')
plt.savefig("charts/100StackedBarChart.png")
