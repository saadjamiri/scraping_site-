# Importation des bibliothèques nécessaires
import requests
# URL de l'API pour récupérer les citations
api_url = 'https://quotes.toscrape.com/api/quotes?page='

# Initialisation
page = 1
quotes = []
has_next_page = True

# Boucle pour parcourir les pages
while has_next_page:
    # Requête GET pour chaque page
    response = requests.get(api_url + str(page))
    data = response.json()  # On obtient la réponse en JSON
    
    # Ajout des citations de la page courante
    quotes.extend(data['quotes'])
    
    # Vérifie s'il y a une page suivante
    has_next_page = data['has_next']
    page += 1  # Passe à la page suivante

# Afficher le nombre total de citations
print()
print(f"Nombre total de citations : {len(quotes)}")
print()
print('*'*12)
# Afficher la première citation et la cinquième citations
print('la première citation est : ',quotes[0]['text'])
print('-'*12)
print('la cinquième citation est : ',quotes[4]["text"])