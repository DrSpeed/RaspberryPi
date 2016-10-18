import plotly.plotly as py
import plotly.graph_objs as go
from time import localtime, strftime

now =  strftime("%Y-%m-%d %H:%M:%S", localtime())



data = [go.Bar(
              x=[str(now)],
              y=[1])]

#py.plot(data, filename = 'camera_shot')

plot_url = py.plot(data, filename = 'camera_shot')

#plot_url = py.plot(data, filename = 'camera_shot', fileopt='extend')
