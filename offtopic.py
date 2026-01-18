d = {"nom": "Alice", "âge": 25, "ville": "Paris", "profession": "développeur"}


# Affiche chaque clé du dictionnaire sur une ligne distincte.

for key in d:  # print keys
    print(key)

for cle in d.keys():
    print(cle)

# Affiche chaque valeur du dictionnaire sur une ligne distincte.

for key in d:  # print values
    print(d[key])

for valeur in d.values():
    print(valeur)

# Affiche à la fois la clé et la valeur (clé: valeur) sur une seule ligne.

for key in d:
    print(key + ":" + str(d[key]))

for cle, valeur in d.items():
    print(f"{cle}: {valeur}")

# Exercice 2: Filtrage des éléments d’un dictionnaire

# Crée un dictionnaire avec des informations sur des étudiants et leurs notes :

etudiants = {"Lucas": 15, "Alice": 18, "Pierre": 10, "Marie": 12, "Sophie": 19}


# Utilise .items() pour afficher les noms et les notes des étudiants qui ont eu plus de 15 sur 20.

for nom, note in etudiants.items():
    if note >= 15:
        print(f"{nom} : {note}")


# Utilise .values() pour compter combien d’étudiants ont eu plus de 15.
total = 0
for note in etudiants.values():
    if note > 15:
        total += 1
print(f"total = {total}")


# Exercice 3: Utilisation de .keys() pour la recherche

# Crée un dictionnaire qui contient des informations sur des films et leurs années de sortie :

films = {
    "Inception": 2010,
    "The Dark Knight": 2008,
    "Interstellar": 2014,
    "Memento": 2000,
    "Dunkirk": 2017,
}


# Utilise .keys() pour vérifier si le film "Interstellar" est dans le dictionnaire.

for nom in films.keys():
    if nom == "interstellar":
        print(True)
        break

# Utilise .keys() pour afficher tous les films sortis avant 2010.

for nom, annee in films.items():
    if annee < 2010:
        print(nom)
        break
