## Écrivez votre code ici !
def square(value):
    try:
        total = value * value
        return total
    except TypeError:
        print("Le paramètre doit être un nombre !")
        return None

        # if type(value) != int and type(value) != float:
        #     print("Le paramètre doit être un nombre !")
        #     return None


print(square("C"))
