from scipy.io import arff
import pandas as pd
import numpy as np
import klasifikator as kf

podatki = arff.loadarff('dataset_61_iris.arff')[0]
podatki = pd.DataFrame(podatki)
podatki = np.asarray(podatki)

slovar = {b'Iris-virginica': 0, b'Iris-setosa': 1, b'Iris-versicolor': 2}
st_razredov = 3
podatki = podatki.T
razredi = []
for podatek in podatki[-1]:
    razredi.append(slovar[podatek])
podatki[-1] = np.asarray(razredi)
podatki = podatki.T

# np.random.shuffle(podatki)

bloki = np.array_split(podatki, 10)
rezultati_evalvacij = []

# naredimo 10 blokov, trening in razvrstitev testnega vzorca
for a in range(10):
	test = bloki[a]
	trening = np.copy(bloki)
	trening = np.delete(trening, a, axis=0)
	trening = np.concatenate(trening, axis=0)
	razredi = kf.sortiraj_po_razredih(trening, st_razredov)
	povp_razred, std_razred, velikost_razredov = kf.statistika(razredi)

	d, p = len(test), 0
	for podatek in test:
		verjetnosti = kf.razvrsti(podatek, st_razredov, povp_razred, std_razred,
								            velikost_razredov)
		if podatek[-1] == verjetnosti.index(max(verjetnosti)):
			p += 1
	rezultati_evalvacij.append(p/d)
zanesljivost = np.sum(rezultati_evalvacij)*10

print(zanesljivost)