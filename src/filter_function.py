avail_units = {
    '101' : {
        'bedrooms' : 3,
        'bathrooms' : 2,
        'price' : 1625
    },
    '215' : {
        'bedrooms' : 2,
        'bathrooms' : 1,
        'price' : 1550
    },
    '231' : {
        'bedrooms' : 1,
        'bathrooms' : 1,
        'price' : 1400
    },
    '431' : {
        'bedrooms' : 2,
        'bathrooms' : 1,
        'price' : 1500
    },
    '1422' : {
        'bedrooms' : 2,
        'bathrooms' : 1,
        'price' : 1350
    },
}

def my_filter(unit_num):
    if avail_units[unit_num]['price'] < 1600 and avail_units[unit_num]['bedrooms'] >= 2:
        return True
    else:
        return False

x = list(filter(my_filter, avail_units))

print(x)