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

# mera za preciznost in občutljivost
# po stolpcih arraya: true positive, false positive, false negative za posamezen razred
tp_fp_fn = np.zeros((3, 3))

# tabela napacnih napovedi - po vrstah predikcije, po stolpcih resnicna pripadnost
tabela_napacnih_napovedi = np.zeros((3, 3))

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
		maksimum = verjetnosti.index(max(verjetnosti))
		if podatek[-1] == maksimum:
			p += 1
			tabela_napacnih_napovedi[maksimum][maksimum] += 1
			tp_fp_fn[maksimum][0] += 1 # dodajanje true positive
		else:
			tp_fp_fn[maksimum][1] +=1 # dodajanje false positive
			tp_fp_fn[podatek[-1]][2] += 1 # dodajanje false negative
			tabela_napacnih_napovedi[maksimum][podatek[-1]] += 1

	rezultati_evalvacij.append(p/d)

zanesljivost = np.sum(rezultati_evalvacij) * 10
preciznost_po_razredih = []
obcutljivost_po_razredih = []
for a in range(len(tp_fp_fn)):
	preciznost = tp_fp_fn[a][0] / (tp_fp_fn[a][0] + tp_fp_fn[a][1])
	obcutljivost = tp_fp_fn[a][0] / (tp_fp_fn[a][0] + tp_fp_fn[a][2])
	preciznost_po_razredih.append(preciznost)
	obcutljivost_po_razredih.append(obcutljivost)

tekst1 = "Zanesljivost s prečnim preverjanjem je {odstotek} %.".format(odstotek = zanesljivost)
tekst2 = "Obcutljivost po razredih je {seznam}.".format(seznam = obcutljivost_po_razredih)
tekst3 = "Preciznost po razredih je {seznam}.".format(seznam = preciznost_po_razredih)
tekst4 = "Tabela napačnih napovedi:"
print(tekst1)
print(tekst2)
print(tekst3)
print(tekst4)
print(tabela_napacnih_napovedi)
print("Opozorilo! Vrednosti se lahko spremenijo do 2%, če podatke "
	  "drugače razvrstimo po blokih. (Uporabi np.random.shuffle v 19. vrstici.)")