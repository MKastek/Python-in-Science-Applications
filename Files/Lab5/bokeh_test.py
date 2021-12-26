from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import numpy as np

#output_notebook()
x = np.linspace(-20 * np.pi, 20 * np.pi,1000)
y_sin = np.sin(x)
y_cos = np.cos(x)

data = {'x': x, 'y_sin': y_sin, 'y_cos': y_cos}

fig = figure(x_range = (-np.pi, np.pi),x_axis_label ='x', y_axis_label='y', title = 'Mój mega wykres',sizing_mode= 'stretch')
fig.toolbar.logo = None
fig.toolbar.autohide = True
fig.grid.grid_line_dash = (6, 5)


fig.circle(x,y_sin, color='red',radius = 0.01 * x)
fig.line(x, y_sin)

show(fig)