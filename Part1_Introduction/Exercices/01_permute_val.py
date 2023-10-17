a = 1
b = 2

print(f" a: {a} b: {b}")

t = a 

a = b 
b = t  # valeur a 

print(f" a: {a} b: {b}")

a = 1
b = 2
c = 3
print(f" a: {a} b: {b} c: {c}")

t = a 

a = b 
b = c 
c = t 

print(f" a: {a} b: {b} c: {c}")


# En Python 
print("-----------------------------------------")

a = 1
b = 2
c = 3
print(f" a: {a} b: {b} c: {c}")

a, b, c = b, c, a # l'assignation par décomposition 

print(f" a: {a} b: {b} c: {c}")
