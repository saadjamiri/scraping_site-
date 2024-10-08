# Projet de Web Scraping - Extraction de Données depuis Quotes to Scrape

## Contexte du Projet

Ce projet consiste à concevoir un script en Python pour extraire et structurer des données provenant d'une page web à l'aide de techniques de **Web Scraping**. Le projet utilise des bibliothèques comme **BeautifulSoup** et **Requests** afin de récupérer et traiter les informations d'un site web.

### Objectifs

L'objectif principal est d'extraire des informations pertinentes depuis le site [Quotes to Scrape](https://quotes.toscrape.com/), et de répondre à plusieurs problématiques telles que :

1. **Nombre de livres et prix moyen dans chaque catégorie :**
   - Cette question est posée pour chaque catégorie disponible sur le site.

2. **Nombre de pages sur le site web :**
   - Identifier combien de pages sont disponibles sur le site à scruter.

3. **Nombre total de citations sur l'URL :**
   - Calculer combien de citations sont affichées sur la page web.

4. **Récupération de la première et de la cinquième citation sur la page :**
   - Extraire et afficher ces citations spécifiques.

5. **Tag le plus répété sur la page :**
   - Analyser et identifier le tag le plus utilisé parmi les citations présentes sur la page.

---

## Prérequis

Avant de commencer à utiliser ce projet, assurez-vous d'avoir les éléments suivants installés :

- **Python 3.x** : Ce projet utilise Python pour automatiser les tâches de scraping.
- **Bibliothèques Python requises** :
  - `requests` : Pour envoyer des requêtes HTTP et obtenir le contenu de la page web.
  - `beautifulsoup4` : Pour analyser et extraire les données du HTML.

### Installation des bibliothèques requises

Vous pouvez installer les dépendances nécessaires à l'aide de `pip` :

```bash
pip install requests
pip install beautifulsoup4
