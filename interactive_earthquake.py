import pandas as pd
import plotly.express as px
import os

project_root = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(project_root, 'data', 'new_eq_data.csv')

df = pd.read_csv(filename)
df = df[['latitude', 'longitude', 'mag']].dropna()

fig = px.scatter_geo(df, lat='latitude', lon='longitude', size='mag', color='mag',
                     hover_name='mag', projection='natural earth',
                     title='全球近期地震分布（可旋转/缩放）',
                     color_continuous_scale='Reds')
fig.update_geos(showcountries=True, countrycolor="Black", showocean=True, oceancolor="LightBlue")
fig.show()