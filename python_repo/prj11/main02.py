# 함수 형태
'''
def 함수이동(매개변수):
    실행할코드
    실행할코드
    실행할코드
    return 값
'''

# 매개변수parameter ㄴㄴ, 변환값return ㄴㄴ
def hello():
    print("hello")
    print("world")
hello()
#
# # 파라미터parameter ㅇㅇ, 변환값return ㄴㄴ
def hello(x):
    print(f"{x}님 welcome~!!!")
hello("최희윤")

# #숫자 두개를 더해서
def print_plus_result(a,b):
    result = a = b
    print(result)
print_plus_result(3,4)

# 파라미터parameter ㄴㄴ, 변환값return ㅇㅇ
def get_number():
    return 10
x = get_number()
print(x)

# 파라미터parameter ㅇㅇ, 리턴return ㅇㅇ
def plus_ten(x):
    result = x + 10
    return result
a = plus_ten(3)
print(a)