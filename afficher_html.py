# Importation des bibliothèques nécessaires
import requests
from bs4 import BeautifulSoup
# Définition de l'URL cible
url = 'https://quotes.toscrape.com/'  
# Envoi d'une requête HTTP GET
reponse = requests.get(url)
# Parsing du contenu HTML avec BeautifulSoup
html = BeautifulSoup(reponse.text,'html.parser')
# Imprimer tout le html 
print(html.prettify())