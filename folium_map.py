import folium

map = folium.Map(location=[20.5, 78.9], zoom_start=4, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[28.7041,77.1025], popup="Delhi", icon=folium.Icon(color="red")))
fg.add_child(folium.Marker(location=[19.0760,72.8777], popup="Mumbai", icon=folium.Icon(color="red")))

map.add_child(fg)
map.save("MAp1.html")
print(map)
