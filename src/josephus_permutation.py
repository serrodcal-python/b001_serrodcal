# def solution(array, k):
#     permutation = []
#     index = 0
#     while array:
#         index = (index + k - 1) % len(array)
#         item = array.pop(index)
#         permutation.append(item)
#     return permutation

from collections import deque

def solution(array, k):
    d = deque(array)
    permutation = []
    while d:
        d.rotate(1 - k)
        item = d.popleft()
        permutation.append(item)
    return permutation

import time
soldiers = 1_000_000
arr = [s+1 for s in range(soldiers)]
k = 3 
start = time.perf_counter()
perm = solution(arr, k)
stop = time.perf_counter()
print(stop - start)