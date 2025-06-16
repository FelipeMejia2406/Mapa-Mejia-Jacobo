import folium# ...existing code...

ubicacion = [18.463127, -69.304883]  # Coordenadas de la Ciudad de México
mapa = folium.Map(location=ubicacion, zoom_start=12)
folium.Marker( ubicacion, popup='Mejia Jacobo Food Truck 🍔').add_to(mapa)
mapa.save('mapa_san_pedro_de_macoris.html')




