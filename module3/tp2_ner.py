"""Named-entity recognition with SpaCy"""

from collections import defaultdict
import sys

import spacy
from spacy.lang.fr.examples import sentences 

nlp = spacy.load('fr_core_news_sm')

n = 100000

# Rem : pour n, 100000 ne fonctionnait pas : le programme était directement tué

def search():
    text = open("1929.txt", encoding='utf-8').read()[:n]
    doc = nlp(text)
    location = defaultdict(int)
    people = defaultdict(int)
    organisation = defaultdict(int)
    for ent in doc.ents:
        if ent.label_ == "LOC" and len(ent.text) > 3:
            location[ent.text] += 1
        elif ent.label_ == "PER" and len(ent.text) > 3:
            people[ent.text] += 1
        elif ent.label == "ORG" and len(ent.text) > 3:
            organisation[ent.text] += 1   
        else :  
            continue 
    sorted_location = sorted(location.items(), key=lambda kv: kv[1], reverse=True)
    sorted_people = sorted(people.items(), key=lambda kv: kv[1], reverse=True)
    sorted_organisation = sorted(organisation.items(), key=lambda kv : kv[1], reverse=True)
    for org, freq in sorted_organisation[:20]:
        print(f"{org}, an organisation, appears {freq} times in the corpus")
    for loc, freq in sorted_location[:20]:
        print(f"{loc}, a location, appears {freq} times in the corpus")
    for person, freq in sorted_people[:20]:
        print(f"{person}, a person, appears {freq} times in the corpus")

# PB : ORG ne semble pas avoir été détecté.. Pourtant, en utilisant le code qui suit, des entitées taggées comme "ORG" sont bien présentes : 
# for ent in doc.ents:
#   print(ent.label_, ' | ', ent.text)

if __name__ == "__main__":
    try:
        if sys.argv[1] == "search":
            search()
        else:
            print("Unknown option, please use 'search'")
    except IndexError:
        print("No option, please specify 'search'")
