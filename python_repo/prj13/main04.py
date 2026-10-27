# 도서관리 프로그램

class Book:
    def __init__(self , a ,b):
        self.title = a
        self.price = b

book_list = []

def print_menu():
    print("메뉴를 선택하세요.")
    print("0. exit")
    print("1. insert")
    print("2. select")

def insert():
    print("제목과 가격을 입력해주세요")
    t = input("title : ")
    p = input("price : ")
    x = Book(t,p)
    book_list.append(x)

def select():
    for x in book_list:
        print(f"제목은 {x.title}이고 , 가격은 {x.price}원 입니다.")

while True:
    print_menu()
    n = int(input("menu : "))
    match n:
        case 0:
            print("종료하겠습니다.")
            break
        case 1:
            insert()
        case 2:
            select()
