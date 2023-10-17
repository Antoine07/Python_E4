# 005 01 Fonction max

def myMax(a, b):
    if a > b :
        return a
    
    return b 

print( myMax(10, 3) )
print( myMax(10, myMax(5, myMax(7, 0))) )


# 005 02

phrase = "Mississippi"
# structure de données qui permet d'avoir un système de clé/val
l = {}

# on parcours la chaine de caractères
for el in phrase:
    # on teste si la clé e existe dans l, si elle existe on ajoute +1 pour la compter 
    if el in l:
        l[el] = 1 + l[el]
    else:
         l[el] = 1

print(l)

