import requests as requests

"""
Premier test de mon api, voici le défi de ce petit algorithme,
Trouver le sujet du texte que j'ai récupéré sur cette page : https://fr.wikipedia.org/wiki/Orientation_du_papier_toilette
"""

text = """
Orientation du papier toilette
Article
Discussion
Lire
Modifier
Modifier le code
Voir l’historique
Orientation du papier toilette

L'orientation par-dessus.

L'orientation par-dessous.
Deux orientations du papier toilette sont possibles lorsque est utilisé un dérouleur de papier toilette d'axe horizontal parallèle à la cloison (ou sur un axe perpendiculaire à la cloison placé latéralement devant l'utilisateur) : le papier toilette peut pendre par-dessus ou en dessous du rouleau. Le choix est surtout question de préférence personnelle et est dicté par l'habitude. Dans les enquêtes, entre 60 % et 70 % des consommateurs américains ou des spécialistes des salles de bains et cuisines répondent qu'ils préfèrent l'orientation par-dessus1.

Ce qui surprend certains observateurs, en particulier la chroniqueuse Ann Landers (en), est de constater à quel point les gens ont des opinions bien arrêtées sur un sujet aussi trivial. Les défenseurs de l'une ou l'autre des positions citent des avantages allant de l'esthétique, l'hospitalité, la propreté, l'économie de papier jusqu'à la facilité avec laquelle on peut détacher les feuilles. D'un côté comme de l'autre, on trouve des célébrités et des experts. Il existe de nombreuses théories sur ce que pourrait révéler la préférence d'une personne : l'âge, le sexe, le statut socio-économique ou l'orientation politique ; un aperçu de certains traits de la personnalité comme la fiabilité ou la flexibilité ; enfin, il pourrait y avoir une corrélation entre ce choix et le fait de posséder un camping-car ou un chat2,3.

Les solutions vont du compromis à l'utilisation de dérouleurs distincts, voire de salles de bains entièrement séparées. Un passionné connu (Bill Jarrett) préconise un plan où son pays adopterait un standard imposant une seule orientation[réf. nécessaire] ; par ailleurs, un inventeur nommé Curtis Batts espère résoudre le problème en popularisant un nouveau type de dérouleur de papier toilette, capable de pivoter d'une orientation à l'autre, système breveté qu'il a présenté au salon INPEX (en) en 19994.

Vers la fin du xxe siècle, la controverse est devenue un mème Internet, repris à l'envi sur la toile5.
""".lower().replace(',', '').split()

response = requests.get("https://iziapi.herokuapp.com/api/stopwords/english").json()
data = set(response)

wordsFiltered = []

for word in text:
    if word not in data:
        wordsFiltered.append(word)

print(wordsFiltered[:3])
