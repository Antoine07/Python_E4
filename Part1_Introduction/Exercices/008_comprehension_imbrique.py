
r = []

for i in range(1, 3):
    for j in range(1, 5):
        r.append((i, j))

print(r)

# Transofmer cela en compréhention de liste

r = [ (i, j) for i in range(1, 3) for j in range(1, 5) ]

print(r)