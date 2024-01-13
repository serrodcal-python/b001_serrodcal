def make_even(num):
    if num % 2 == 1:
        return num + 1
    else:
        return num
    
x = [551, 641, 891, 122, 453, 223, 234, 343, 562, 115, 554, 111, 679, 516]

# y = []
# for num in x:
#     y.append(make_even(num))

# y = list(map(make_even, x))
y = [make_even(num) for num in x] # Easier to read

print(y)