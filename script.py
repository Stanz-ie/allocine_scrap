import os
import requests
import csv
from bs4 import BeautifulSoup

# 1. Faire une requête GET pour charger la page et stocker le HTML

url = 'https://www.allocine.fr/film/sorties-semaine/'
reponse = requests.get(url)

if reponse.status_code == 200:
    html_content = reponse.content
    # récupération du HTML de la page
else:
    print("Impossible de récupérer la page")


# 2. Analyser le HTML 
soup = BeautifulSoup(html_content, "lxml")

# 3. Extraire les données

titres = soup.find_all("h2", {"class": "meta-title"})
for titre in titres:
    print(titre.text)

'''
infos = soup.find_all('h2', {"class": "meta meta-affinity-score"})
for info in infos:
    description_film = info.text.strip()
    print(description_film)
'''
# 4. Enregistrer les données dans un fichier csv

with open("donnees.csv", "w", encoding="utf-8") as fichier:
    writer = csv.writer(fichier)

i = 0
with open("donnees.csv", "w", encoding="utf-8") as fichier:
    writer = csv.writer(fichier)
    while i < len(titres):
        writer.writerow((titres[i].text))
        i+=1



