# Fonction calculate_average
def calculate_average(numbers):
    somme = 0
    for num in numbers:
        somme += num
    coef = len(numbers)
    moyenne = somme / coef
    return moyenne


# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
