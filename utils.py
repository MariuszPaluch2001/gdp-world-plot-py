import geopandas as gpd
import pandas as pd
import json

def read_geodata_file(shapefile):
    return gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]

def clean_gdf(gdf):
    gdf.columns = ['country', 'country_code', 'geometry']
    index = int(gdf[gdf['country'] == 'Antarctica'].index[0])
    gdf.drop(index)

def read_csv(filename, usecols, skiprows):
    return pd.read_csv(filename, usecols = usecols, skiprows = skiprows)

def merge(gdf, dataframe, left_on, right_on):
    return gdf.merge(dataframe, left_on = left_on, right_on = right_on)

def merge_to_data(merged):
    merged_json = json.loads(merged.to_json())
    return json.dumps(merged_json)