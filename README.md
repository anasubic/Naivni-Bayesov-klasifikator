# Naivni Bayesov klasifikator

<h4>Opis projekta</h4>
Naivni ''Bayesov klasifikator'' je klasifikacijski algoritem strojnega učenja. Koda je implementirana samo z uporabo knjižnice Numpy. 

<h4>Uporaba</h4>
Potrebne knjižnice: Numpy,  Pandas in Scipy.io. 
<br/>
Klasifikator sprejema podatke tipa ARFF, ki jih uvedemo v program <code>evaluacija.py</code> kot 

<code>podatki = arff.loadarff('nasa_datoteka.arff')[0]</code>.
Vsi dobljeni rezultati že vključujejo metodo
prečnega preverjanjanja na desetih blokih.

<h4>Evaluacija</h4>
Evaluacija je narejena na podatkih Iris Dataset (3 razredi, 4 parametri). Rezultati so že prečno preverjeni, vendar se lahko zanesljivost spremeni še za do 2 %, če so podatki drugače razporejeni po blokih. Za drugačno razporeditev od začetne se uporabi funkcija <code>
np.random.shuffle(podatki)
</code> v 19. vrstici. 

<h4>Rezultati za Iris Dataset</h4>

<h5>Zanesljivost</h5>

| Zanesljivost |
|--------------|
| 94,67 %      |

<h5>Preciznost</h5>

| Razred       | Iris Virginica    | Iris Setosa    | Iris Versicolor    |
|--------------|------|------|------|
| **Preciznost** | 0.92 | 1.00 | 0.92 |

<h5>Občutljivost</h5>


| Razred       | Iris Virginica    | Iris Setosa    | Iris Versicolor    |
|--------------|------|------|------|
| **Občutljivost** | 0.92 | 1.00 | 0.92 |

<h5>Tabela napačnosti</h5>

| predicted\actual | Iris Virginca | Iris Setosa | Iris Versicolor |
|------------------|---------------|-------------|-----------------|
| **Iris Virginca**    | 46            | 0           | 4               |
| **Iris Setosa**      | 0             | 50          | 0               |
| **Iris Versicolor**  | 4             | 0           | 46              |


<h4>Viri</h4>

* [https://en.wikipedia.org/wiki/Naive_Bayes_classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
* [https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/](https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/)
* [https://en.wikipedia.org/wiki/Precision_and_recall](https://en.wikipedia.org/wiki/Precision_and_recall)
* [https://en.wikipedia.org/wiki/Confusion_matrix](https://en.wikipedia.org/wiki/Confusion_matrix)
* [https://archive.ics.uci.edu/ml/datasets/Iris](https://archive.ics.uci.edu/ml/datasets/Iris)
* [https://www.openml.org/d/61](https://www.openml.org/d/61)


* Dodatna pomoč: David Lajevec (nekaj uporabnih vrstic za lažje delo s podatki, npr. slovar, da dobimo številsko poimenovane razrede, transponiranje).  [https://github.com/davidlajevec](https://github.com/davidlajevec)

