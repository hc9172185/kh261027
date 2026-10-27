# 0~9 중에서 짝수만 출력
x = 0
while x < 10:
    x = x + 1
    if x % 2 == 1:
        continue
    print(x)

