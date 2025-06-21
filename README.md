# AI28-projet : Sujet 3 - Prédiction de niveau de revenus

L'objectif de ce projet en trinôme est de traiter un problème de machine learning à l'aide d'un jeu de données réelles.

## Architecture du projet

### Jupyter notebook

Le projet contient deux jupyter notebooks :

- **AED.ipynb** : correspond à l'ensemble du code lié à l'analyse exploratoire des données.
- **entrainement.ipynb** : correspond à l'ensemble du code lié aux pré-traitement, à l'entrainement et à l'évaluation des modèles de machine learning.

**Attention** : l'exécution du notebook `entrainement.ipynb` peut prendre un temps significativement long en particulier pour les modèles : AdaBoosting, Stacking et SVM. Temps d'exécution sur un M1 Air : 62 minutes.

### Fichier Python :

Un fichier Python `AED_utils.py` contient du code nécessaire à l'exécution du notebook `AED.ipynb`. A conserver à la racine du projet.

### Autres :

- requirements.txt : pour installer les dépendances.
- /figures : dossier contenant l'ensemble des figures générées sous format .png.
- ai28-rapport-bcv.pdf : fichier rapport écrit sous format .pdf.

## Installer le projet

Ce projet est un notebook Jupyter contenant des analyses ou du code Python. Toutes les dépendances nécessaires sont listées dans le fichier `requirements.txt`.

1. **Cloner le dépôt :**

   ```bash
   git clone https://gitlab.utc.fr/ai28_tp_projet/ai28-projet.git
   cd votre-projet
   ```

2. **Créer un environnement virtuel :**
   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
   ```
3. **Installer les dépendances :**
   Exécuter à la racine du projet
   ```bash
   # S'assurer d'être dans l'environnement virutel
   pip install -r requirements.txt
   ```
4. **Lancer Jupyter Notebook :**
   ```bash
   jupyter notebook
   ```

### Prérequis :

- Python 3.7 ou plus
- pip
- Jupyter Notebook
- (optionnel) virtualenv

## Composition du groupe

| Groupe 2 - BCV   |
| ---------------- |
| Alexandre Bidaux |
| Julie Chartier   |
| Quentin Valakou  |

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

Nous choisissons de les télécharger via le site web..

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
