"""Exploring the corpus"""

from collections import defaultdict
from collections import Counter
import os

import matplotlib.pyplot as plt
import numpy as np

import re


my_words=["cimetière", "cimetieres", "cimetiere", "cimetières"]

path = "../data/txt/"
files = sorted(os.listdir(path))

dic = defaultdict(int)

for txt_file in files:
    if "_" in txt_file:
        elems = txt_file.split("_")
        year = elems[1]
        logfile = open(path+txt_file, "r") 
        for line in logfile:
            line = re.sub(r'[^\w\s]', '', line) # regex permettant de garder les alphanumériques et les espaces
            for word in my_words:
                if word in line.lower().split():
                    dic[year] += 1
    else:
        print(f"Anomalous file: {f}")
print(dic)

def plot_bar():
    index = np.arange(len(dic))
    plt.bar(index, dic.values())
    plt.xlabel('Années')
    plt.ylabel('nombre d\'utilisations du mot cimetière')
    plt.xticks(index, dic.keys(), fontsize=10, rotation=90)
    plt.title('Évolution du nombre de fois où "cimetière" apparaît')
    plt.show()

plot_bar()
