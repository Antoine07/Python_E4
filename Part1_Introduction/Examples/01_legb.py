
# Localement E G Builtins

# Global
a = 1  # définit Globalement

# Une fonction 
# def + le nom de la fonction 
def foo():
    # Fonction englobante
    c = 100
    def bar():

        b = 10 # définit Localement
        # on fait appelle aux symboles a et b 
        print(a, b, c, __debug__ ) # Englobant 

    # On l'appelle (exécution) dans la fonction
    bar()


# Appelle de la fonctio foo dans l'espace dans lequelle est définie 
foo()

