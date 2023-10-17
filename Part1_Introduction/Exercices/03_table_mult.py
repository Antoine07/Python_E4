

def mult(num):
    assert isinstance(num, int), "La tva n'est un int" 

    l = []
    for i in range(1, 11):
        l.append(i*num)

    return l 

print(mult(5))
print(mult(6))