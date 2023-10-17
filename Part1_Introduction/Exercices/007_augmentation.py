"""
### 007 Exercice compréhesion de liste

1. A l'aide d'une compréhension de liste augmenter de 10% chaque valeur

2. Puis faites une nouvelle augmentation de 5% sur les valeurs supérieur à 50.
"""

l = [0, 1, 100, 4, 9, 16, 25, 36, 49, 64, 81]   

# 1. 
l = [ round( e*1.1, 2 ) for e in l ]
print(l)

# 2. 

l = [ round( e*1.05, 2 ) if e > 50 else e for e in l ]
print(l)
