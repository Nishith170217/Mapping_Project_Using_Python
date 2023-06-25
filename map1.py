import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#colored marker
def color_producers(elev):
    if elev<1500:
        return "green"
    elif 1500<=elev and elev<2400:
        return "orange"
    else:
        return "red"
#print(lat)
map = folium.Map(location=[40.393106, -113.110520],zoom_start=4)
fg= folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lon,elev):
#fg.add_child(folium.Marker(location=[23.828296, 90.405122], popup="Airport", icon=folium.Icon(color='red')))
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius= 6, popup=str(el) +" m", fill_color=color_producers(el), color = "grey", fill_opacity = 0.8))
#22.780399, 89.876453
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']< 10000000 
else 'orange' if 10000000<= x['properties']['POP2005']< 20000000 else 'red'}))

map.add_child(fg)
map.save("Map1.html")