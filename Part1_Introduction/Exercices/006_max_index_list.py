"""
Cette fonction retourne le max et son indice dans la liste de nombre

"""

l = [0, 1, 100, 4, 9, 16, 25, 36, 49, 64, 81]   

def maxList(l):
    assert type(l) == list and len(l) > 0, "error type list or empty list"

    m, j = l[0], 0
    for i in range(1, len(l)) :
        if l[i] > m :
            m, j = l[i], i

    return { 'max' : m, 'indice' : j }

try:
    print(maxList([]))
except AssertionError as e:
    print(e)
