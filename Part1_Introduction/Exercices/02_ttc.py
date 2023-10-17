

def ttc(price, tva = 0.2 ):

    assert isinstance(tva, float), "La tva n'est un float" 
    assert isinstance(price, float), "Le price n'est un float" 

    # casting => forcer le type des variables
    price, tva = float(price), float(tva)

    return round( price * (1 + tva), 2 )

# tout en float 
try:
    print(ttc(100.00))
    print(ttc(100., .3))
    print(ttc(100., ".3"))
    print(ttc(100., "bonjour"))
except AssertionError:
    print("ERROR DE TYPE")

print("On peut continuer à faire du python ")