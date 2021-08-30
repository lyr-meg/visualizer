from bokeh.plotting import figure
from bokeh.io import output_file, show, curdoc
from bokeh.layouts import row, widgetbox, column
from bokeh.models import DateRangeSlider, ColumnDataSource, CustomJS
from datetime import date
import datetime
import pandas as pd

# Specify the name of the output file and show the result
# output_file('positive_mentions.html')

data = pd.read_csv('test.csv')
data['Month of Year'] = pd.to_datetime(data["Month of Year"])
source = ColumnDataSource(data = {"x": data["Month of Year"], "y": data["Positive Mentions"]})

# Create a figure with x_axis_type="datetime": p
p1 = figure(x_axis_type="datetime", x_axis_label='Month of Year', y_axis_label='Positive Mentions')

# Plot date along the x axis and price along the y axis
p1.line("x", "y", line_width=2, source=source)
# With date on the x-axis and price on the y-axis, add a white circle glyph of size 4
p1.circle("x", "y", fill_color='white', size=4, source=source)

# p2 = figure(x_axis_type="datetime", x_axis_label='Month of Year', y_axis_label='Negative Mentions')
# p2.line(df['Month of Year'], df['Negative Mentions'], line_width=2)
# p2.circle(df['Month of Year'], df['Negative Mentions'], fill_color='white', size=4)

def date_range_update(attr, old, new):
    date_range = date_range_slider.value
    d1 = datetime.datetime.fromtimestamp(date_range_slider.value[0]/1000)
    d2 = datetime.datetime.fromtimestamp(date_range_slider.value[1]/1000)
    print(d1, d2)
    new_data = {
    'x'       : data.loc[(data["Month of Year"]>d1)&(data["Month of Year"]<d2)]["Month of Year"],
    'y'       : data.loc[(data["Month of Year"]>d1)&(data["Month of Year"]<d2)]["Positive Mentions"]
    }
    source.data = new_data

# callback = CustomJS(args=dict(x_range=fig.x_range), code="""
# var start = cb_obj.get("value");
# x_range.set("start", start);
# x_range.set("end", start+2);
# """)

date_range_slider = DateRangeSlider(value=(date(2016, 1, 1), date(2019, 6, 1)),\
                  start=date(2016, 1, 1), end=date.today())
date_range_slider.on_change('value', date_range_update)

layout = column(widgetbox(date_range_slider), p1)

curdoc().add_root(layout)
curdoc().title = 'Positive and Negative Mentions'

# show(slide)
