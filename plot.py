from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar
from bokeh.palettes import brewer

def bokeh_plot(json_data, field):
    geosource = GeoJSONDataSource(geojson = json_data)
    palette = brewer['YlGnBu'][8]
    palette = palette[::-1]
    color_mapper = LinearColorMapper(palette = palette, low = 0, high = 40000)
    color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8,width = 500, height = 20,
    border_line_color=None,location = (0,0), orientation = 'horizontal')
    p = figure(title = 'GPD 2021', plot_height = 600 , plot_width = 950, toolbar_location = None)
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    p.patches('xs','ys', source = geosource,fill_color = {'field' : field, 'transform' : color_mapper},
            line_color = 'black', line_width = 0.25, fill_alpha = 1)
    p.add_layout(color_bar, 'below')
    show(p)
