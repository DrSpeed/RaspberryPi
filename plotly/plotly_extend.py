import plotly.plotly as py
from plotly.graph_objs import *

new_data = Scatter(x=[5, 6], y=[21, 22] )

data = Data( [ new_data ] )

plot_url = py.plot(data, filename = 'basic-line', fileopt='extend')
