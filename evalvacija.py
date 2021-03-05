from scipy.io import arff
import pandas as pd
import numpy as np
import klasifikator as kf

podatki = arff.loadarff('dataset_61_iris.arff')[0]
podatki = pd.DataFrame(podatki)
podatki = np.asarray(podatki)

slovar = {b'Iris-virginica':0, b'Iris-setosa':1, b'Iris-versicolor':2}
podatki = podatki.T
prevedeno = np.copy(podatki[-1])
for k, v in slovar.items(): prevedeno[podatki[-1]==k] = v
podatki[-1] = prevedeno
podatki = podatki.T

delitev = 0.3
dolzina_podatkov = len(podatki)
np.random.shuffle(podatki)
test, train = np.split(podatki, [int(dolzina_podatkov*delitev)])

povp_razred, std_razred, velikost_razredov = kf.statistika(kf.sortiraj_po_razredih(train, 3))
st_razredov = len(velikost_razredov)

p, d = 0, len(test)
for podatek in test:
	verjetnosti = kf.razvrsti(podatek,st_razredov,povp_razred,std_razred,velikost_razredov)
	if podatek[-1] == verjetnosti.index(max(verjetnosti)):
		p += 1

print("Pravilno: " + str(round((p/d)*100,2)) + "%")
