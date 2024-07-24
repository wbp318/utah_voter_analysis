# Utah Voter Analysis Project

## Overview
This project aims to analyze and visualize voter data for the state of Utah, focusing on Salt Lake, Weber, Davis, and Utah counties. It uses Python to process geospatial data and create informative maps of voter registration and electoral patterns.

## Features
- Map generation of Utah counties
- Voter registration data visualization
- Analysis of voting patterns (to be implemented)
- Integration of publicly distributed voter data from the state of Utah

## Prerequisites
- Python 3.12
- Git (for version control)

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/your-username/utah-voter-analysis.git
   cd utah-voter-analysis
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   .\venv\Scripts\Activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Upgrade pip and install wheel:
   ```
   python -m pip install --upgrade pip setuptools wheel
   ```

4. Install required packages:
   ```
   python -m pip install numpy==1.26.2
   python -m pip install pandas==2.1.4
   python -m pip install matplotlib==3.8.2
   python -m pip install pyproj==3.6.1
   python -m pip install Shapely==2.0.2
   python -m pip install Fiona==1.9.5
   python -m pip install pyogrio==0.7.2
   python -m pip install geopandas==0.14.1
   ```

## Usage
1. Ensure your virtual environment is activated.
2. Run the basic map script:
   ```
   python scripts/utah_basic_map.py
   ```
3. To analyze voter data, use:
   ```
   python scripts/utah_voter_map.py
   ```

## Data Sources
- Utah county shapefile: [Source Link]
- Voter registration data: [Source Link]

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
MIT LICENSE

## Contact
William Parker - wbp93623@gmail.com

Project Link: https://github.com/your-username/utah-voter-analysis