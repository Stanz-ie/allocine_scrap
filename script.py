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


# 2. Parser les données avec lxml

soup = BeautifulSoup(html_content, "lxml")
#print(soup.prettify())

# 3. Extraire les données


titres = soup.find_all("h2", {"class": "meta-title"})
infos = soup.find_all("div", {"class": "meta-body-item meta-body-direction"})

# 4. Utiliser la fonction zip pour regrouper les données de titres et celles d'infos

for titre, info in zip(titres, infos):
    print(titre.text.strip(), info.text.strip())

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


'''