inv = ['Gem', 'Sword', 'Shield', 'Health Potion']

indx = inv.index('Gem')
item = inv.pop(indx)
inv.append(item)

print(inv)