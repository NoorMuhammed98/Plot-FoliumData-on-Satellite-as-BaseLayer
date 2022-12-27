import folium

start_loc = (24,67)
style_function = lambda x: {'fillColor': '#FF0000'}

m = folium.Map(start_loc,zoom_start=16)

tile = folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = False,
        control = True
       ).add_to(m)

folium.GeoJson(r'....D:\Data\X_Town.geojson',name="X Town",popup=folium.GeoJsonPopup(fields=["Category"])).add_to(m)
folium.LayerControl().add_to(m)

m.save(r'....D:\Folium_maps\m.html')