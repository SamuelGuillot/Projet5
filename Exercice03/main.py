words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

liste_comprehension = []
for x in words:
    nombre_voyelle = 0
    for char in x:
        if char.lower() in "aeiouy":
            nombre_voyelle += 1

    liste_comprehension.append((x, nombre_voyelle))

print(liste_comprehension)


# words = ["python", "samuel", "sofien"]

# def count_vowels_in_words(words):
#     return [(word, sum(1 for char in word if char.lower() in "aeiouy")) for word in words]


# count_vowels_in_words(words)
