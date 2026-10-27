def f01(x):
    result = x(100)
    print(result)

def plus_one(n):
    return n+1

f01(lambda num : num + 1)