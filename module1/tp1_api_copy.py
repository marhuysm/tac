"""Adaptation du script s3_api.py pour interroger l'API bxl_bourgmestres https://opendata.bruxelles.be/api/v1/console/datasets/1.0/search/"""

import json
import sys

import requests

def test():
    print("hello!")

def show_info():
    print ("test")

def print_info(name):
    """Rercherche d'informations liées aux bourgemestres"""
    osm = "https://opendata.bruxelles.be/api/records/1.0/search/"
    data = {'dataset': 'bxl_bourgmestres', 'q' : name, 'format':'json'}
    resp = requests.get(osm, data)
    json_list = json.loads(resp.text)
    print("Number of documents found: ", json_list['nhits'], end='\n')
    for bgRecord in json_list['records']:
        print('=== ', bgRecord['fields']['bourgmestres'], ' ===', end='\n')
        try:
            print('\t- Date de naissance: ', bgRecord['fields']['date_de_naissance'], end='\n')
        except KeyError:
            pass

        try:
            print('\t- Date de deces: ', bgRecord['fields']['decede'], end='\n')
        except KeyError:
            pass

        try:
            print('\t- Début de mandat: ', bgRecord['fields']['debut_de_mandat'], end='\n')
        except KeyError:
            pass
        try:
            print('\t- Date d\'entrée en fonction de bourgmestre ou de 1er échevin ff: ', bgRecord['fields']['date_d_entree_en_fonction_de_bourgmestre_ou_de_1er_echevin_ff'], end='\n')
        except KeyError:
            pass

        try:
            print('\t- Arrêté royal de nomination: ', bgRecord['fields']['arrete_royal_de_nomination'], end='\n')
        except KeyError:
            pass
    
        try:  
            print("\t- Date d'installation: ", bgRecord['fields']['date_d_installation'], end='\n')
        except KeyError:
            pass
   
        try:
            print("\t- Fin de fonction: ", bgRecord['fields']['fin_de_fonction'], end='\n')
        except KeyError:
            pass
    
        try:
            print('\t- Date de démission: ', bgRecord['fields']['date_de_demission'], end='\n')
        except KeyError:
            pass

        try:
            print('\t- Date de fin de fonction: ', bgRecord['fields']['fin_de_fonction'], end='\n')
        except KeyError:
            pass

        

if __name__ == "__main__":
    name = input("Entrez le nom du bourgemestre pour lequel vous cherchez une information : ")
    while (name != "" and name != "exit"):
        print_info(name)
        name = input("Entrez le nom du bourgemestre pour lequel vous cherchez une information : ")

    print("== END ==")

