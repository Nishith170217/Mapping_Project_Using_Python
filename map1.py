import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
#print(lat)
map = folium.Map(location=[40.393106, -113.110520],zoom_start=4)
fg= folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lon,elev):
#fg.add_child(folium.Marker(location=[23.828296, 90.405122], popup="Airport", icon=folium.Icon(color='red')))
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el) +" m", icon=folium.Icon(color='green')))
#22.780399, 89.876453

map.add_child(fg)
map.save("Map1.html")