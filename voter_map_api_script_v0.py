import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import requests
from shapely.geometry import shape

def load_utah_counties():
    counties = gpd.read_file('data/utah_counties.shp')
    print("All counties:", counties['NAME'].tolist())
    # Filter for the specific counties
    counties_of_interest = ['Weber', 'Davis', 'Salt Lake', 'Utah', 'Summit']
    filtered_counties = counties[counties['NAME'].isin(counties_of_interest)]
    print(f"Filtered counties: {filtered_counties['NAME'].tolist()}")
    return filtered_counties

def load_voter_data_from_api():
    url = "https://opendata.utah.gov/resource/fs6s-ucmf.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        
        # Create geometry column directly from the_geom
        df['geometry'] = df['the_geom'].apply(lambda geom: shape(geom))
        
        # Create GeoDataFrame
        gdf = gpd.GeoDataFrame(df, geometry='geometry')
        
        # Set CRS (assuming WGS84, modify if different)
        gdf.set_crs(epsg=4326, inplace=True)
        
        # Filter for the specific counties
        counties_of_interest = ['27', '6', '18', '25', '22']  # County IDs for Weber, Davis, Salt Lake, Utah, Summit
        filtered_gdf = gdf[gdf['countyid'].isin(counties_of_interest)]
        print(f"Unique county IDs in data: {gdf['countyid'].unique()}")
        print(f"Filtered county IDs: {filtered_gdf['countyid'].unique()}")
        return filtered_gdf
    else:
        raise Exception(f"Failed to fetch data: HTTP {response.status_code}")

def create_voter_map(counties, precincts):
    fig, ax = plt.subplots(figsize=(20, 15))
    
    if counties.empty:
        print("Warning: Counties GeoDataFrame is empty.")
    else:
        # Plot counties
        counties.plot(ax=ax, edgecolor='black', facecolor='none')
    
    if precincts.empty:
        print("Warning: Precincts GeoDataFrame is empty.")
    else:
        # Plot precincts
        precincts.plot(ax=ax, column='precinctid', cmap='viridis', alpha=0.7)
    
    ax.set_title('Utah Election Precincts Map\n(Weber, Davis, Salt Lake, Utah, and Summit Counties)', fontsize=16)
    ax.axis('off')
    
    # Set the extent of the map to the bounds of the data
    if not counties.empty:
        bounds = counties.total_bounds
    elif not precincts.empty:
        bounds = precincts.total_bounds
    else:
        print("Warning: Both counties and precincts are empty. Unable to set map extent.")
        return fig, ax
    
    ax.set_xlim(bounds[[0, 2]])
    ax.set_ylim(bounds[[1, 3]])
    
    plt.tight_layout()
    return fig, ax

if __name__ == "__main__":
    utah_counties = load_utah_counties()
    precinct_data = load_voter_data_from_api()
    
    print("Counties info:")
    print(utah_counties.info())
    print("\nPrecinct data info:")
    print(precinct_data.info())
    
    fig, ax = create_voter_map(utah_counties, precinct_data)
    plt.show()

    print(f"Number of precincts plotted: {len(precinct_data)}")
    print("Precinct data columns:", precinct_data.columns)