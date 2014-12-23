# coding: utf-8

import json
from geopy import geocoders

gc = geocoders.GoogleV3()

datos = json.load(open('proyectos.js'))
items = datos.get('items')
centros = {}


for it in items:
    c = it.get('centro')
    print c
    if c not in centros:
        loc = gc.geocode(c + u" Aragon, España")
        if loc: centros[c] = [loc.address, loc.longitude, loc.latitude]

json.dump(centros, open('centros.js', 'w'))
