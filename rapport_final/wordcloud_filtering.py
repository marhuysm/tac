"""Filter out stopwords for word cloud"""

import sys
import nltk
try:
    from nltk.corpus import stopwords
except LookupError:
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
       "page", "petite", "voyez", "voulu", "pouvait", "vingt", "égard", "vol", "zijn", "heeft", "commune", "communes", "juin"]
sw = set(sw)


def filtering(year):
    path = f"{year}.txt"
    output = open(f"{year}_keywords.txt", "w")

    with open(path) as f:
        text = f.read()
        words = nltk.wordpunct_tokenize(text)
        kept = [w.lower() for w in words if len(
            w) > 2 and w.isalpha() and w.lower() not in sw]
        kept_string = " ".join(kept)
        output.write(kept_string)


if __name__ == '__main__':
    year = sys.argv[1]
    filtering(year)
