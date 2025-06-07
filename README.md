# AI28-projet : Sujet 3 - Prédiction de niveau de revenus

L'objectif de ce projet en trinôme est de traiter un problème de machine learning à l'aide d'un jeu de données réelles.

## Composition du groupe

| Groupe 2 - BCV | 
| ----------- | 
| Alexandre Bidaux| 
| Julie Chartier| 
| Quentin Valakou|

## Récupération des données
Deux façons existent afin de récupérer les données sur lesquelles nous travaillons : les télécharger sur le site web UCI Machine Learning Repository ou les télécharger via la librairie python comme suit :

```
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
adult = fetch_ucirepo(id=2) 
  
# data (as pandas dataframes) 
X = adult.data.features 
y = adult.data.targets 
  
# metadata 
print(adult.metadata) 
  
# variable information 
print(adult.variables) 
```
Nous choisissons de les télécharger via la librairie Python.

## Présentation des sources
Les fichiers obtenus se présentent comme suit :
```
.
├── adult.data : jeu de données d'entrainement au format csv (séparateur de colonnes : la virgule)
├── adult.names : fichier donnant du contexte et descriptions sur les données et les opérations ayant été réalisées dessus
├── adult.test : jeu de données de test au format csv (séparateur de colonnes : la virgule)
├── Index : liste les fichiers, leur date de motification et leur taille
└── old.adult.names : ancienne version du fichier adult.names
```

## Sources utilisées
- [Jeu de données Adult](https://archive.ics.uci.edu/dataset/2/adult)