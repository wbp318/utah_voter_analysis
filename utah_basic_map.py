import geopandas as gpd
import matplotlib.pyplot as plt
import os
import xml.etree.ElementTree as ET

def check_shapefile_components(base_path):
    extensions = ['.shp', '.shx', '.dbf', '.prj', '.cpg', '.shp.xml']
    missing = []
    for ext in extensions:
        if not os.path.exists(base_path + ext):
            missing.append(ext)
    if missing:
        print(f"Warning: The following shapefile components are missing: {', '.join(missing)}")
    else:
        print("All expected shapefile components are present.")

def load_utah_counties():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    shapefile_base = os.path.join(current_dir, 'data', 'utah_counties')
    
    # Check for all shapefile components
    check_shapefile_components(shapefile_base)
    
    # Load shapefile
    counties = gpd.read_file(shapefile_base + '.shp')
    
    # Load metadata from XML if needed
    xml_path = shapefile_base + '.shp.xml'
    if os.path.exists(xml_path):
        tree = ET.parse(xml_path)
        root = tree.getroot()
        # Here you can extract any needed metadata from the XML
        # For example:
        # metadata = root.find('.//metadata')
        # if metadata is not None:
        #     print("Metadata found in XML")
    
    return counties

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