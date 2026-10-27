n = int(input())
result = 0
for x in range(1, n+1):
    if x % 2 == 0:
        result += x
print(result)