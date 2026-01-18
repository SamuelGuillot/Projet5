## Écrivez votre code ici !
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Nom: {self.name}")
        print(f"Âge: {self.age}")


class Employe(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"Salaire: {self.salary}")


person = Person("Alice", 30)
person.display_details()

print("--------------------")

employe = Employe("Vikktor", 40, 5000)
employe.display_details()

# MRO classes
