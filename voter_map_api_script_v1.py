import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import requests
from shapely.geometry import shape
import os

def load_utah_counties():
    counties = gpd.read_file('data/utah_counties.shp')
    print("All counties:", counties['NAME'].tolist())
    counties_of_interest = ['Weber', 'Davis', 'Salt Lake', 'Utah', 'Summit']
    filtered_counties = counties[counties['NAME'].isin(counties_of_interest)]
    print("Filtered counties:", filtered_counties['NAME'].tolist())
    return filtered_counties

def load_voter_data_from_api():
    url = "https://opendata.utah.gov/resource/fs6s-ucmf.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['geometry'] = df['the_geom'].apply(lambda geom: shape(geom))
        gdf = gpd.GeoDataFrame(df, geometry='geometry')
        gdf.set_crs(epsg=4326, inplace=True)
        counties_of_interest = ['27', '6', '18', '25', '22']
        filtered_gdf = gdf[gdf['countyid'].isin(counties_of_interest)]
        print("Unique county IDs in precinct data:", filtered_gdf['countyid'].unique())
        return filtered_gdf

def create_voter_map(counties, precincts):
    fig, ax = plt.subplots(figsize=(20, 15))
    
    # Plot counties
    counties.plot(ax=ax, edgecolor='black', facecolor='none', linewidth=2)
    for idx, row in counties.iterrows():
        ax.annotate(row['NAME'], xy=(row.geometry.centroid.x, row.geometry.centroid.y),
                    ha='center', va='center', fontsize=12, fontweight='bold')

    # Plot precincts
    precinct_plot = precincts.plot(ax=ax, column='countyid', cmap='viridis', alpha=0.7, legend=True)
    
    # Customize legend
    legend = ax.get_legend()
    if legend:
        legend.set_bbox_to_anchor((1.05, 0.5))
        legend.set_title('County ID')
    
    ax.set_title('Utah Election Precincts Map\n(Weber, Davis, Salt Lake, Utah, and Summit Counties)', fontsize=16)
    ax.axis('off')
    
    # Set the extent of the map to the bounds of the counties
    ax.set_xlim(counties.total_bounds[[0, 2]])
    ax.set_ylim(counties.total_bounds[[1, 3]])
    
    plt.tight_layout()
    return fig, ax

if __name__ == "__main__":
    print("Current working directory:", os.getcwd())
    print("Files in 'data' directory:", os.listdir('data'))

    utah_counties = load_utah_counties()
    precinct_data = load_voter_data_from_api()
    
    fig, ax = create_voter_map(utah_counties, precinct_data)
    plt.show()

    print(f"Number of precincts plotted: {len(precinct_data)}")
    print("County names:", utah_counties['NAME'].tolist())
    print("Unique county IDs in precinct data:", precinct_data['countyid'].unique())