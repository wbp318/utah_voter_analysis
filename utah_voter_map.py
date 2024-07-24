# File: utah_voter_map.py

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

def load_utah_counties():
    return gpd.read_file('data/utah_counties.shp')

def load_voter_data(file_path):
    return pd.read_csv(file_path)

def merge_data(counties, voter_data):
    # Adjust the merge columns based on your actual data
    return counties.merge(voter_data, left_on='NAME', right_on='County')

def create_voter_map(merged_data, column_to_plot):
    fig, ax = plt.subplots(figsize=(12, 8))
    merged_data.plot(column=column_to_plot, ax=ax, legend=True,
                     legend_kwds={'label': column_to_plot},
                     cmap='YlOrRd')
    
    # Add county labels with voter data
    for idx, row in merged_data.iterrows():
        ax.annotate(text=f"{row['NAME']}\n{row[column_to_plot]:,}",
                    xy=(row.geometry.centroid.x, row.geometry.centroid.y),
                    ha='center', va='center', fontsize=8)
    
    ax.set_title(f'Utah Counties - {column_to_plot}')
    ax.axis('off')
    plt.tight_layout()
    return fig, ax

if __name__ == "__main__":
    utah_counties = load_utah_counties()
    voter_data = load_voter_data('data/utah_voter_data.csv')
    merged_data = merge_data(utah_counties, voter_data)
    
    # Adjust 'Registered_Voters' to match your actual column name
    fig, ax = create_voter_map(merged_data, 'Registered_Voters')
    plt.show()