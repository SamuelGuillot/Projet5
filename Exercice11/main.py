## Écrivez votre code ici !
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Erreur :Nombre positif svp")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Erreur : solde insuffisant.")
        elif amount <= 0:
            print("Erreur : Nombre positif svp.")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"{self.account_holder} : {self.balance}")


compte = BankAccount("Alice", 1000)
compte.display_balance()
compte.deposit(500)
compte.withdraw(2000)
compte.withdraw(300)
compte.display_balance()
