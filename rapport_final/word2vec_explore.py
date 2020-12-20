from gensim.models import Word2Vec
from pprint import pprint

model = Word2Vec.load("../data/bulletins.model")

word1 = "cimetière"

# Est-ce que le mot est lié à un contexte de travaux, de financement, 
# ou a un contexte de débat politique / religieux ?

word2 = "travaux"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "bâtir"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "rénovation"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "agrandissement"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "déplacer"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "budget"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "financement"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "gestion"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "police"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "caveaux"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "catholique"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "protestant"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "religion"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "citoyen"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "église"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "commune"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "laïque"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "consacré"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "débat"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word1 = "funérailles"

word2 = "catholique"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "laïques"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word1 = "inhumation"

word2 = "église"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")


word1 = "sépulture"

word2 = "catholique"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "laïque"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")



print('Liste des mots les plus similaires à cimetière dans le modèle word2vec:')

pprint(model.wv.most_similar("cimetière"))

print('Liste des mots les plus similaires à caveaux dans le modèle word2vec:')

pprint(model.wv.most_similar("caveaux"))

print('Liste des mots les plus similaires à église dans le modèle word2vec:')

pprint(model.wv.most_similar("église"))

print('Liste des mots les plus similaires à sépulture dans le modèle word2vec:')

pprint(model.wv.most_similar("sépulture"))

print('Liste des mots les plus similaires à inhumation dans le modèle word2vec:')

pprint(model.wv.most_similar("inhumation"))