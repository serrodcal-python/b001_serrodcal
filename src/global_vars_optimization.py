global_var = 10

def bad_func():
    ans = 0
    for i in range(1000):
        # Python copy into local scope each time
        ans += global_var * i
    return ans

def func():
    ans = 0
    local_var = global_var
    for i in range(1000):
        ans += local_var * i
    return ans

func()