### change month name to month int

df['New Month'] = df['Month'].apply(lambda x: month_name_to_int(x))
df['Month of Year'] = pd.to_datetime(df["Year"].astype(str) + '/' + df["New Month"].astype(str))
# df['Month of Year'] = df['Month of Year'].dt.strftime('%Y-%m')




### bokeh plots, refer to the myapp.py file as well
# import necessary libraries
from bokeh.plotting import *
from bokeh.io import output_file, show, curdoc,output_notebook,push_notebook
from bokeh.layouts import row, widgetbox, layout, column, gridplot
from bokeh.models import DateSlider, ColumnDataSource, CustomJS, HoverTool,CategoricalColorMapper
from bokeh.models.widgets import DateRangeSlider, Tabs, Panel
# from bokeh.charts import BoxPlot, output_notebook, show
output_notebook()

from datetime import date
import pandas as pd

# Specify the name of the output file and show the result
output_file('positive_mentions.html')

# use source as data if curdoc is used for creation of a bokeh app
source = ColumnDataSource(data = {"x": df["Month of Year"], "y": df["Positive Mentions"]})

# Create a figure with x_axis_type="datetime": p
p1 = figure(x_axis_type="datetime", x_axis_label='Month of Year', y_axis_label='Positive Mentions')

# Plot date along the x axis and price along the y axis
p1.line("x", "y", line_width=2, source=source)
# With date on the x-axis and price on the y-axis, add a white circle glyph of size 4
p1.circle("x", "y", fill_color='white', size=4, source=source)

p2 = figure(x_axis_type="datetime", x_axis_label='Month of Year', y_axis_label='Negative Mentions')
p2.line(df['Month of Year'], df['Negative Mentions'], line_width=2)
p2.circle(df['Month of Year'], df['Negative Mentions'], fill_color='white', size=4)

# # create bar
# p = BoxPlot(df, values = "Protein", label = "Category",
#             color = "yellow", title = "Protein Summary (grouped by category)",
#              legend = "top_right")

# # show the results
# show(p)

# def date_range_update(attr, old, new):
#     date_range = date_range_slider.value
#     new_data = {
#     'x'       : df["Month of Year"].loc[date_range[0]:date_range[1]],
#     'y'       : df["Positive Mentions"].loc[date_range[0]:date_range[1]]
# #     'point'      : data.loc[date_range[0]:date_range[1]].pointLabel,
# #     'direction'      : data.loc[date_range[0]:date_range[1]].directionKey
#     }
#     source.data = new_data

# date_range_slider = DateRangeSlider(value=(date(2016, 1, 1), date(2019, 6, 1)), \
#                   start=date(2016, 1, 1), end=date.today())
# date_range_slider.on_change('value', date_range_update)

# layout = column(widgetbox(date_range_slider), p1)

# curdoc().add_root(layout)
# curdoc().title = 'Positive and Negative Mentions'

layout = row(p1, p2)
show(layout)


bokeh serve --show --port 5022 myapp.py





#######################
``` github style markdown in jupyter notebook
resp = requests.get(zip_url, stream=True, proxies=proxyDict)
resp.status_code
resp.json()['dictionary key']
stream parameter: by default, when you make a request, the body of the response is \
downloaded immediately. You can override this behaviour and defer \
downloading the response body until you access the Response.content \
attribute with the stream parameter

# create file save paths with os, and create folders if don't exist
APP_DIR = os.path.join(os.path.dirname(os.path.abspath("__file__")), "../..")
DATA_DIR = "data/raw_data/CAN_Unemployment_Rate"
SAVE_DIR = os.path.join(APP_DIR, DATA_DIR)

# download a zip file
resp = requests.get(zip_url, stream=True, proxies=proxyDict)
    if resp.status_code == 200:
        zipped_content = zipfile.ZipFile(BytesIO(resp.content))
        zipped_content.extractall(SAVE_DIR) #Must save and reload. Cannot unzip into memory.
