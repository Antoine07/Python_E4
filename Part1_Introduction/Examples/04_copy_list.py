l = [1,2,3,4,5]
m = l # l'assignation de ne fait pes de copie des objets en général
m[0] = 100
print(l) 
print('------')
print(m) 

print('------')

# shallow copy de la première liste dans une autre variable 

l = [1,2,3,4,5]

r = l[:] # shallow copy
r[0] = 100

print(l) 
print('------')
print(r) 

print('------')

# attention la shallow copy ne marche pas pour les sous référence
l = [[1, 2], [3, 4], [5, 6]]

# shallow copy ne fait la copie que de la première 
r = l[:]
r[0][0] = 100

print(l) 
print('------')
print(r) 