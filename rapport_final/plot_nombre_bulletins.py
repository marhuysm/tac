"""Exploring the corpus"""

from collections import defaultdict
import os

import matplotlib.pyplot as plt
import numpy as np

path = "../data/txt/"
dic = defaultdict(int)
dic2 = defaultdict(int)
all_years = [str(year) for year in range(1847, 1979)]
covered_years = set()

files = sorted(os.listdir(path))
for f in files:
    if "_" in f:
        elems = f.split("_")
        year = elems[1]
        dic[year] += 1
    else:
        print(f"Anomalous file: {f}")
print(dic)

def plot_bar():
    index = np.arange(len(dic))
    plt.bar(index, dic.values())
    plt.xlabel('Année')
    plt.ylabel('nombre de bulletins')
    plt.xticks(index, dic.keys(), fontsize=10, rotation=90)
    plt.title('Évolution du nombre de bulletins')
    plt.show()

plot_bar()
