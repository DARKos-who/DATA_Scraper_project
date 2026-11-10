# DATA Scraper Project

## Installation

Cloner le dépôt, puis créer un environnement Python dans le dossier du projet :

    git clone https://github.com/DARKos-who/DATA_Scraper_project.git
    cd DATA_Scraper_project
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Avant chaque nouvelle session de travail dans ce dossier :

    git pull

## Nettoyage des données

Ouvrir `data_cleaning.ipynb` dans VS Code, sélectionner le noyau Python de `.venv`, puis exécuter les cellules dans l'ordre.

- `RAW_scraped_data.csv` : données brutes produites par le scraper.
- `cleaned_data.csv` : 362 lignes conservées, avec les URL séparées du texte des liens.
- `content_frequencies.csv` : 238 éléments distincts avec leur nombre d'occurrences.

Les lignes répétées restent dans `cleaned_data.csv` : elles peuvent représenter plusieurs apparitions du même texte sur la page. Certains textes collés proviennent de l'extraction HTML et ne sont pas corrigés automatiquement.

Le scraper collecte les titres, paragraphes et liens d'une page. Il ne crée pas de fiches produit structurées avec prix et catégorie.

**Attention :** relancer `Scraper.py` depuis le dossier du projet remplace `RAW_scraped_data.csv`.

## Visualisation des données

Ouvrir `visualisation_des_donnees.ipynb` dans VS Code, sélectionner le noyau Python de `.venv`, puis exécuter les cellules dans l’ordre. Le notebook charge `cleaned_data.csv` et présente six graphiques réalisés avec Matplotlib et Seaborn : types d’éléments, longueur des textes, comparaison par type, textes répétés, mots des titres H3 et domaines des liens. Chaque graphique est accompagné d’une interprétation. Le notebook se termine par les conclusions, les limites des données et un plan pour une présentation orale d’environ sept minutes.

Les données décrivent le contenu textuel d’une page à un moment donné. Elles ne contiennent ni ventes, ni prix structurés, ni catégories de produits fiables.
