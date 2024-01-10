# def func(array):
#     for i in array:
#         if i == 0:
#             array.remove(i)
#             array.append(0)
#     return array

# arr = [1,2,0,3,0,4,5]

def func(array):
    t = []
    z = 0
    for i in array:
        if i != 0:
            t.append(i)
        else:
            z += 0
    t.extend(z * [0])
    return t

import random
import time

n=200000
arr = [random.randint(0, 9) for _ in range(n)]

start = time.time()
print(func(arr))
stop = time.time()

print(stop-start)