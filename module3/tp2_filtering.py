"""Filter out stopwords for word cloud"""

import sys
import nltk
from nltk.corpus import stopwords

sw = stopwords.words("french")
sw += ["les", "plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout",
       "ils", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous",
       "celle", "entre", "encore", "toutes", "pendant", "moins", "dire", "cela", "non",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres",
       "van", "het", "autre", "jusqu", "ville bruxelles", "ville", "bruxelles", "de",
       "mesdames", "messieurs", "bourgmestre", "bourgmestres", "cependant", "franc",
       "grand", "part", "pense", "chose", "trè", "toute","avant", "parce", "parce que",
       "ville de bruxelles", "conseil communal", "conseil", "communal","aucune", "ici",
       "trop", "etc", "lequel", "laquelle", "question", "alors","lorsque", "suivant",
       "car", "côté", "puis", "rue", "toujours", "seulement", "son", "sa", "ses", "leurs",
       "notamment", "pourrait", "frai", "quant", "façon", "crois","quelque","peu", "celui",
       "celle","ceux","celles", "certain", "certaine", "certains", "certaines","grand", "grande",
       "grands", "sujet", "peuvent", "beaucoup", "exemple", "aujourd'hui", "fait", "faite", "quelques",
       "objet", "pourquoi", "comment", "quel", "très", "voir", "proposer", "même", "mêmes", "pourra",
       "mois", "demande", "donner", "monsieur", "madame", "arrêté", "lieu", "rien", "actuellement", "elles",
       "ils", "nombre", "cas", "né", "née", "faites", "nouveau", "nouvelle", "concerne", "nécessaire", "francs",
       "francs francs", "sens", "dernier", "chaque", "tout", "toute", "résultat", "raison", "dite", "collège",
       "communal", "ancien", "demander", "suite", "possible", "seul", "tableau dessous", "doit", "doivent",
       "conclusions rapport", "dessus", "dessous", "devant", "matière", "égard", "donné", "demandé", "avis",
       "avis favorable", "propose vote", "vote", "modification", "article", "vue", "aucun", "point vue",
       "jamais", "émettre","prendre", "établir", "émettre avis", "également", "ensemble", "vient", "agit", "considérable",
       "politique", "première", "premier", "prévu", "fin", "quand", "ordre", "commune", "catégorie", "voudrais", "tant",
       "mettre", "pouvons", "devoir", "produit", "lorsqu", "déjà", "moment", "année", "point", "compris", "telle",
       "mot", "ailleurs", "nécessaires", "estime", "effet", "puisque", "pouvoir", "endroit", "total", "quelle", "abord",
       "proposition", "existe", "jour", "conclusion", "section", "concernant", "kilogramme kilogrammes", "kilogramme", "kilogrammes",
       "trouve", "permettre", "accord", "aujourd hui", "autant", "condition", "million"]
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
