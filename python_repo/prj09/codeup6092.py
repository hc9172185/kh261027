# 이상한 출척 번호 부르기1

# 선생님이 부른 출석번호 리스트에 잘 받아적는
n = input()
x = input()
num_list = x.split()

# 메모장 준비
memo = [0] * 24

# 출석 부른거 보고 메모장 수정
for student_num in num_list:
    student_num = int(student_num)
    memo[student_num] = int(memo[student_num])+1

# 결과 확인
for x in memo[1:24]:
    print(x , end=" ")