
phones = [
    { 'name': "iphone XX", 'priceHT': "900EURO" },
    { 'name': "iphone X", 'priceHT': "70EURO" },
    { 'name': "iphone B", 'priceHT': "200EURO" },
]

phones = [{'name': phone['name'], 'priceHT': float( phone['priceHT'].replace('EURO', '') ) } for phone in phones ]

print(phones)


print("--------")

phones = [
    { 'name': "iphone XX", 'priceHT': "900EURO" },
    { 'name': "iphone X", 'priceHT': "70EURO" },
    { 'name': "iphone B", 'priceHT': "200EURO" },
]

# def sanitizeEuro(phones):

#     for phone in phones:
#        phone['priceHT'] = float( phone['priceHT'].replace('EURO', '') )


# sanitizeEuro(phones)
# print(phones)

# le map il itére sur chaque valeur de la liste, une logique pour un item de la liste
def sanitizeEuro(phone):
    return { 'name' : phone['name'] , 'priceHT' : float( phone['priceHT'].replace('EURO', '') ) }

print( list(map(sanitizeEuro, phones)) )