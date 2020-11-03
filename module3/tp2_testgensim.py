raw_corpus = ["Localement, du reste, d'aucune manière, les bases du règlement actuel et constitueront, au contraire, des améliorations.",
"Le Collège vous propose un nouveau règlement sur les inhumations.",
"Le règlement ancien date déjà de cinquante ans et, en cours de route, nous avons dû prendre une série d'ordonnances pour mettre en application des mesures jugées indispensables",
"D'autre part, au cimetière d'Evere, i l n'y a pas de cryptes, tandis que nous en possédons au cimetière de Laeken",
"Nous avons profité de la revision du règlement pour y insérer des clauses qui régiront, à l'avenir, les cryptes de Laeken",
"Je profite de l'occasion pour protester au nom du groupe socialiste quant à l'élaboration des ordres du jour par le Collège",
"Il y a 67 points cà l'ordre du jour, y compris l'objet n° 22 qui comporte 28 articles, ce qui nous mène à un ordre du jour de 100 points",
"Je pense qu'on ne devrait pas attendre si longtemps pour convoquer le Conseil communal",
"Si les objets, comme le règlement sur les inhumations et transports funèbres, avaient plus d'importance, nous serions dans l'impossibilité de les examiner d'une façon complète. A u nom du groupe socialiste, je tenais à élever cette protestation",
"A la page 25, dans le texte nouveau de l'article 35 , vous dites ceci",
"Les porteurs quittent le convoi après la cérémonie religieuse ou, s'il s'agit de transports civils, après la levée du corps, à quelque distance de la maison mortuaire",
"L'ancien texte porte",
"Les porteurs quittent le convoi aux limites de la Ville",
"Nous demandons le maintien de l'ancien texte",
"Nous estimons qu'il ne faut pas faire de différence entre une cérémonie civile et une cérémonie religieuse",
"Il faut que les familles des défunts soient traitées sur un pied d'égalité",
"Je vais prendre chacun des articles"]

# Create a set of frequent words
stoplist = set('le la les du des et au vous un une sur de en avons avez qui y il elle eux nous je faut que qu pour sur dans aux à l a collège communal bruxelles laeken'.split(' '))
# Lowercase each document, split it by white space and filter out stopwords
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in raw_corpus]

# Count word frequencies
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

# Only keep words that appear more than once
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]

from gensim import corpora

dictionary = corpora.Dictionary(processed_corpus)
print(dictionary.token2id)

new_doc = "règlement cimetière transports convoi"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_vec)


bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
bow_corpus

from gensim import models
# train the model
tfidf = models.TfidfModel(bow_corpus)
# transform the "system minors" string
tfidf[dictionary.doc2bow("system minors".lower().split())]