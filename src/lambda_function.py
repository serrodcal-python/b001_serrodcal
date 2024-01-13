def add(x, y):
    return x + y

print(add(4, 5))

add2 = lambda x,y: x+y
print(add2(4, 5))

print((lambda x,y: x+y)(4,5))

def my_map(my_func, my_iter):
    result = []
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)
    return(result)


nums = [3, 4, 5, 6, 7]

cubed = my_map(lambda x: x**3, nums)

print(cubed)
