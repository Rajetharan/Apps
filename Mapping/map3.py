import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])

def colour_producer(elevation):
    if elevation < 1000:
         return 'green'
    elif 1000  <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location = [40.77,-111.89], zoom_start = 6,  tiles = "Stamen Toner")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el,name in zip(lat,lon,elev,name):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius = 6, popup = str(el) + "m",
    fill_color=colour_producer(el), color = 'grey', fill_opacity = 0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x ['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map_html_circle.html")
