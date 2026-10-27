print('====match case====')

# 숫자 1 ~ 12 입력받아서
# 해당 월의 마지막 일 출력

x = int(input("month : "))
match x:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31")
    case 2:
        print("28")
    case 4 | 6 | 9 | 11:
        print("30")
    case _:
        print(f"입력하신 {x}월은 존재하지 않습니다.")
