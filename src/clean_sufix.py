links = ['www.serrodcal.io', 'www.google.com', 'www.wikipedia.com']

for link in links:
    # print(link.lstrip('www.')) # Same with 'w.', because looking any 'w'
    print(link.removeprefix('www.'))