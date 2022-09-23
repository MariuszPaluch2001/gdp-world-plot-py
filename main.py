from utils import read_geodata_file, clean_gdf, read_csv, merge, merge_to_data
from plot import bokeh_plot

gdf = read_geodata_file('data/world_110m/ne_110m_admin_0_countries.shp')
clean_gdf(gdf)

df = read_csv('data/gdb_world.csv', ['Country Name', 'Country Code', '2021' ], 3)


merged = gdf.merge(df, left_on = 'country_code', right_on = 'Country Code')
merged = merge(gdf, df, 'country_code', 'Country Code')

json_data = merge_to_data(merged)

bokeh_plot(json_data, '2021')


