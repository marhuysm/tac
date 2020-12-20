"""Adaptation du script s3_api.py pour interroger l'API https://opendata.bruxelles.be/explore/dataset/cimetieres/information/
et https://opendata.bruxelles.be/explore/dataset/monuments-funeraires-du-cimetiere-de-laeken/information/"""

import json
import sys
from pprint import pprint   # pretty-print

import requests

def print_info(cimetieres):
    """Rercherche d'informations liées aux cimetières : récupérer la localisation"""
    osm = "https://opendata.bruxelles.be/api/records/1.0/search/"
    data = {'dataset': 'cimetieres','format':'json'}
    resp = requests.get(osm, data)
    json_list = json.loads(resp.text)
    print("Number of cemeteries found: ", json_list['nhits'], end='\n')
    for CimRecord in json_list['records']:
        try:
            print('\t- commune: ', CimRecord['fields']['commune'], end='\n')
        except KeyError:
            pass

        try:
            print('\t- Coordonnées: ', CimRecord['fields']['geo_coordinates'], end='\n')
        except KeyError:
            pass

def print_info_bis(monuments):
    """Rercherche d'informations liées aux monuments : récupérer la localisation"""
    osm = "https://opendata.bruxelles.be/api/records/1.0/search/"
    data = {'dataset': 'monuments-funeraires-du-cimetiere-de-laeken','format':'json'}
    resp = requests.get(osm, data)
    json_list = json.loads(resp.text)
    print("Number of funeral monuments found: ", json_list['nhits'], end='\n')
    for MonRecord in json_list['records']:
        try:
            print('\t- Nom de monument: ', MonRecord['fields']['monument'], end='\n')
        except KeyError:
            pass

        try:
            print('\t- Coordonnées: ', MonRecord['fields']['geocoordinates'], end='\n')
        except KeyError:
            pass


cimetieres = '*'
monuments = '*'
print_info(cimetieres) 
print_info_bis(monuments) 


# Requête qui permet de savoir qu'il y a 4 cimetières reconnus à Bruxelles, et d'avoir leurs coordonnées
# permet également d'avoir la localisation de 20 monuments du cimetière de laeken
# Peut être exploité par la suite, si l'on a par exemple plus de données, si les bdd sont plus complètes, 
# ou comme une base si l'on veut créer une visualisation des monuments et de l'espace funéraire à Bruxelles.
