import folium
map = folium.Map(location=[23.828296, 90.405122],zoom_start=7)
fg= folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[23.828296, 90.405122], popup="Airport", icon=folium.Icon(color='red')))
fg.add_child(folium.Marker(location=[22.780399, 89.876453], popup="My Home", icon=folium.Icon(color='green')))
#22.780399, 89.876453
map.add_child(fg)
map.save("Map1.html")