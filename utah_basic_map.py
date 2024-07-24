# File: utah_basic_map.py

import geopandas as gpd
import matplotlib.pyplot as plt

def load_utah_counties():
    # Load the Utah counties shapefile
    return gpd.read_file('data/utah_counties.shp')

def create_utah_map(counties):
    fig, ax = plt.subplots(figsize=(12, 8))
    counties.plot(ax=ax, edgecolor='black', facecolor='none')
    
    # Add county labels
    for idx, row in counties.iterrows():
        ax.annotate(text=row['NAME'], xy=(row.geometry.centroid.x, row.geometry.centroid.y),
                    ha='center', va='center', fontsize=8)
    
    ax.set_title('Utah Counties Map')
    ax.axis('off')
    plt.tight_layout()
    return fig, ax

if __name__ == "__main__":
    utah_counties = load_utah_counties()
    fig, ax = create_utah_map(utah_counties)
    plt.show()