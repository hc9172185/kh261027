#이상한 출척 번호2
n = input()
x = input()
num_list = x.split()

for i in range(int(n)-1, -1, -1):
    print(num_list[i], end=" ")