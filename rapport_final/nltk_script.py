import nltk
import os

nltk.download('stopwords')

from nltk.corpus import stopwords

sw = stopwords.words("french")
sw += ["les", "plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout", 
       "ils", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous",
       "celle", "entre", "encore", "toutes", "pendant", "moins", "dire", "cela", "non",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres",
       "van", "het", "autre", "jusqu", "bulletins", "communal", "bulletin" "communale", "bulletin", "rue", "conseil", "francs",
       "budget", "projet", "franc", "frais", "somme", "avis", "finances", "total", "cas", "jour",
       "partie", "lieu", "ville", "collège", "bruxelles", "section", "séance", "bourgmestre", "rapport",
       "prix", "année", "grand", "mois", "propose", "recettes", "elle", "elles", "très", "mètres", "celui",
       "messieurs", "administration", "demande", "service", "question", "echevin", "communal", "dépenses",
       "proposition", "place", "chez", "mars", "janvier", "quelle", "bonne", "même", "puisse", "telle", "lequel", "tel", "laquelle",
       "faisant", "ligne", "toute", "nombre", "honorable", "point", "communale", "point", "discussion", "membres", "commission",
       "part", "donner", "approbation", "ordre", "leurs", "celte", "état", "ceux", "avant", "etc", "hui", "crois", "aujourd", 
       "chaque", "faite", "pourrait", "moyen", "voir", "agit", "parce", "que", "déjà", "aucun", "aucune", "suite", "décembre",
       "grande", "quelques", "dernière","effet", "situation", "suivant", "faite", "plusieurs", "rien", "quatre", "seulement", "pourrait",
       "mai", "années", "pourra", "cent", "car", "alors", "fois", "prendre", "proposer", "plusieurs", "manière", "aucun",
       "aucune", "quand", "toujours", "'accord", "octobre", "septembre", "faites", "quant", "devant", "raison", "doivent",
       "novembre", "haute", "avril", "juillet", "mot", "pouvoir", "peuvent", "cinq", "trouve", "sieur", "cependant", "diverses",
       "chose", "choses", "lorsque", "février", "trop", "août", "côté", "assez", "celles", "six", "donne", "communales",
       "cause", "mettre", "ici", "vient", "demander", "dix", "devoir", "également", "dernières", "quelque", "jamais",
       "voici", "afin", "faits", "présente", "but", "mis", "bon", "puis", "suivants", "pense", "dès", "'ailleurs", 
       "lorsqu'", "pouvons", "mise", "huit", "remarquer", "lors'", "actuellement", "mieux", "pourquoi", "autant", "certain", "certains",
       "certaines", "prochaine", "près", "résulte", "veut", "présent", "rendre", "devront", "seule", "suit", "actuel", "parfaitement", 
       "immédiatement", "choses", "chacun", "mêmes", "delà", "font", "certains", "émis", "fort", "sens", "présents", "existe", "partir", 
       "puisque", "fin", "suivante", "devra", "pourront", "sauf", "maintenant", "seconde", "parties", "paraît", "petit", "tenir", "parole",
       "page", "petite", "voyez", "voulu", "pouvait", "vingt", "égard" ]
sw = set(sw)

path = "../data/all.txt"
limit = 10**8

with open(path, encoding='utf-8') as f:
    text = f.read()[:limit]
    words = nltk.wordpunct_tokenize(text)
    print(f"{len(words)} mots trouvés dans le corpus")
    kept = [w.lower() for w in words if len(w) > 2 and w.isalpha() and w.lower() not in sw]
    voc = set(kept)
    print(f"{len(kept)} mots conservés, ({len(voc)} differentes formes de mots)")
    fdist = nltk.FreqDist(kept)


print ("Mots les plus communs dans le corpus, accompagnés de leur nombre d'utilisations, en dehors des mots-vides et des mots trop courts (cf kept)")
print(fdist.most_common(400))
