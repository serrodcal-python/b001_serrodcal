def merge_arrays(arrayA, arrayB):
    return sorted(set(arrayA + arrayB))

a = [2,6,4,3,2,4,6]
b = [2,4,1,4,6,5,1]
c = merge_arrays(a, b)
print(c)