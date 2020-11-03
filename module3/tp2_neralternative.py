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
    entities = defaultdict(int)
    for ent in doc.ents:
        if len(ent.text) > 3:
            entities[ent.text] += 1  
    sorted_entities = sorted(entities.items(), key=lambda kv : kv[1], reverse=True)
    for ent, freq in sorted_entities[:40]:
        print(f"{ent} appears {freq} times in the corpus")

if __name__ == "__main__":
    try:
        if sys.argv[1] == "search":
            search()
        else:
            print("Unknown option, please use 'search'")
    except IndexError:
        print("No option, please specify 'search'")
