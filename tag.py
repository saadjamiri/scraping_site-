# Importation des bibliothèques nécessaires
import requests
from bs4 import BeautifulSoup
from collections import Counter
# Définition de l'URL cible
url='https://quotes.toscrape.com/tableful/'
# Envoyer une requête GET
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# Exclure la section 'Top Ten tags'
top_ten_tags_section = soup.find('h3', string='Top Ten tags')
# Si la section existe, on l'exclut
if top_ten_tags_section:
    top_ten_tags_section.parent.decompose()  # Supprimer cette section du DOM
#extraire tous les tags
tag_elemnts= soup.find_all('a')
#Récupérer le texte de chaque tag
tags = [tag.text.strip() for tag in tag_elemnts if '/tag/' in tag['href']]
# compter la fréquence de chaque tag 
tag_compt = Counter(tags)
# Trouver le tag le plus fréquent 
most_common_tag = tag_compt.most_common(1)[0]
print()
print(f"Le tag le plus répétitif est '{most_common_tag[0]}' avec {most_common_tag[1]} occurrences.")