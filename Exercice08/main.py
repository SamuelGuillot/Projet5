def log_decorator(func):
    def myinner():
        print(f"Exécution de la fonction '{func.__name__}'")
        func()
        print(f"La fonction '{func.__name__}' est terminée.")

    return myinner


@log_decorator
def function_test():
    print("Je suis une simple fonction.")


function_test()
