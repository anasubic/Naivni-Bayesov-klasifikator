import numpy as np


def sortiraj_po_razredih(podatki, st_razredov):
    razredi = [[] for razred in range(st_razredov)]
    for podatek in podatki:
        razredi[podatek[-1]].append(podatek)
    return razredi

def statistika(razredi):
	povp_razred = []
	std_razred = []
	velikost_razredov = []
	for razred in razredi:
		razred = np.array(np.stack(razred, axis=0), dtype=np.float64)
		povp_razred.append(np.average(razred, axis=0))
		std_razred.append(np.std(razred, axis=0, ddof=1))
		velikost_razredov.append(len(razred))
	return np.asarray(povp_razred), np.asarray(std_razred), np.asarray(velikost_razredov)

def gaussova_porazdelitev(x, povp, std):
	gauss = (1/(std * np.sqrt(2*np.pi)))*np.exp(-1/2*((x - povp)/std)**2)
	return gauss

def razvrsti(podatek_test, st_razredov, povp_razred, std_razred, velikost_razredov):
	velikost_podatkov = np.sum(velikost_razredov)
	vse_verjetnosti = []
	for a in range(st_razredov):
		pojavnost_razreda = velikost_razredov[a] / velikost_podatkov
		verjetnost = pojavnost_razreda
		for b in range(len(podatek_test)-1):
			verjetnost = verjetnost * gaussova_porazdelitev(podatek_test[b],
															povp_razred[a][b], std_razred[a][b])
		vse_verjetnosti.append(verjetnost)
	return vse_verjetnosti
