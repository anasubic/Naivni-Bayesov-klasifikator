import numpy as np

dataset = [[3.393533211,2.331273381,0],
 [3.110073483,1.781539638,0],
 [1.343808831,3.368360954,0],
 [3.582294042,4.67917911,0],
 [2.280362439,2.866990263,0],
 [7.423436942,4.696522875,1],
 [5.745051997,3.533989803,1],
 [9.172168622,2.511101045,1],
 [7.792783481,3.424088941,1],
 [7.939820817,0.791637231,1]]

# razredi od 0 do N, če so drugačni se jih prej prevede s slovarjem
def sortiraj_po_razredih(podatki, st_razredov):
  razredi = [[] for razred in range(st_razredov)]
  for podatek in podatki:
   razredi[podatek[-1]].append(podatek[:-1])
  return np.asarray(razredi)

def statistika(razredi):
 povp_razred = []
 std_razred = []
 velikost_razredov = []
 for razred in razredi:
  povp_razred.append(np.average(razred, axis=0))
  std_razred.append(np.std(razred, axis=0, ddof=1))
  velikost_razredov.append(len(razred))
 #statisticni_podatki = np.asarray([np.asarray(povp_razred), np.asarray(std_razred), np.asarray(velikost_razredov)])
 return np.asarray(povp_razred), np.asarray(std_razred), np.asarray(velikost_razredov)

def gaussova_porazdelitev(x, povp, std):
 gauss = (1/std * np.sqrt(2*np.pi))*np.exp(-1/2*((x - povp)/std)**2)
 return gauss

def verjetnost_pripadnosti_posameznemu_razredu(podatki, podatki_test, st_razredov):
 povp_razred, std_razred, velikost_razredov = statistika(sortiraj_po_razredih(podatki, 2))
 velikost_podatkov = len(podatki_test)
 for x in podatki:
  vse_verjetnosti = []
  for a in range(st_razredov):
   pojavnost_razreda = velikost_razredov[a] / velikost_podatkov
   verjetnost = pojavnost_razreda
   for b in range(len(x)-1):
    verjetnost = verjetnost * gaussova_porazdelitev(b, povp_razred[a][b], std_razred[a][b])
   vse_verjetnosti.append(verjetnost)
  return vse_verjetnosti

for i in range(len(dataset)):
 print(verjetnost_pripadnosti_posameznemu_razredu(dataset, dataset[i], 2))

