# for
# 여러개를 가진 값을 쓸때
# for x in range(1,6):
#     print(x)
# while
# 조건을 하나만 써도 동작이 가능하다.
# 단순히 조건을 써서 반복할때
# continue와 break가 있다.
# break - 날 감싸고 있는 반복문을 탈출한다
# continue - 가장 가까운 반복문 처음으로 돌아간다.
# x = 1
# while x < 6:
#     print(x)
#     x = x + 1
# match case
# if elif else와는 다르게 여러 선택을 하나의 결과를 낸다.
# x = int(input("month: "))
# match x:
#     case 1 | 3 | 5 | 7 | 8 | 10 |12:
#         print("31일")
#     case 2:
#         print("28일")
#     case 4 | 6 | 9 | 11:
#         print("30일")
# 함수 매개변수
# 함수 - 명령어들을 모아놓은 것
# 여러군데 흩어진 같은 작업의 코드를 한번에 묶어놓는다.
# def
# def hello():
#     print("hello world")
# 이 안에 if, while, for 변수 만드는 거 다 쓸 수 있다.ㅋㅋ
#     return 10
# x = hello()
# print(x)

# def hello(abc):
# 값을 받아온 것은 파라미터(매개변수)에 적는다.
# 파라미터의 개수는 여러 개 적을 수 있다.
#     print(abc)
#     return 123
# 반대로 값을 뱉어낸 것은 파라미터 밑에 적는다.
# 리턴은 하나만 나온다.
# x= hello("아무거나")
# print(x)