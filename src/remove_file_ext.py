full_files = ['info.txt', 'image.png', 'app.c', 'info.3.txt', 'image2.jpg']

for file in full_files:
    name = '.'.join(file.split('.')[0:-1])
    print(name)

print()

import os
for file in full_files:
    name = os.path.splitext(file)[0]
    print(name)
