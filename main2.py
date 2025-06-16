import osmnx as ox
import networkx as nx
import folium

# Coordenadas de ejemplo (puedes reemplazarlas por las que necesites)
origen = (19.432608, -99.133209)    # Ejemplo: Ciudad de México
destino = (19.427025, -99.167665)   # Ejemplo: Otro punto en CDMX

# Descargar la red de calles para la zona
G = ox.graph_from_point(origen, dist=3000, network_type='walk')

# Encontrar los nodos más cercanos al origen y destino
origen_nodo = ox.nearest_nodes(G, origen[1], origen[0])
destino_nodo = ox.nearest_nodes(G, destino[1], destino[0])

# Calcular la ruta más corta
ruta = nx.shortest_path(G, origen_nodo, destino_nodo, weight='length')

# Obtener los puntos de la ruta
ruta_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in ruta]

# Crear el mapa con Folium
m = folium.Map(location=origen, zoom_start=14)
folium.Marker(origen, tooltip="Origen").add_to(m)
folium.Marker(destino, tooltip="Destino").add_to(m)
folium.PolyLine(ruta_coords, color="blue", weight=5, opacity=0.7).add_to(m)

# Guardar el mapa en HTML
os.makedirs('output', exist_ok=True)
m.save('output/como_llegar.html')