# 이상한 출석 번호 부르기3

n = input()
x = input()
num_list = x.split()

memo = num_list[0]
for num in num_list:
    memo = int(memo)
    num = int(num)
    if memo > num:
        memo = num

print(memo)