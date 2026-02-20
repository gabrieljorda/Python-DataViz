import folium

mapa = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)

#adicioando marcaçoes para cafeterias 
cafererias = [
    {'localizacao': [-23.561, -46.655], 'nome': 'Café A'},
    {'localizacao': [-23.545, -46.620], 'nome': 'Café B'},
    {'localizacao': [-23.530, -46.640], 'nome': 'Café C'},
    {'localizacao': [-23.555, -46.610], 'nome': 'Café D'},
]

for cafe in cafererias:
    folium.Marker(
        location=cafe['localizacao'],
        popup=cafe['nome'],
        icon=folium.Icon(color='blue',icon='coffee')
    ).add_to(mapa)
    
mapa.save('mapa_cafeterias.html')
