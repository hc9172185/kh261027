# 종료
# 도서 등록
# 도서 조회
from unittest import case

book_list = []

# 독서 종료 등록 조회 메뉴
def print_menu():
    print("=== BOOK ===")
    print("0. exit")
    print("1. insert")
    print("2. select")

# 독서 책과 가격 등록
def insert_book():
    print("===insert book===")
    t = input("title : ")
    c = input("price : ")
    d = {
        "title" : t ,
        "price" : c
    }
    book_list.append(d)
    print("~~~ insert finish ~~~")

# 독서 책과 가격 조회
def select_book():
    print("--- select book ---")
    for d in book_list:
        print(f"{d["title"]} / {d["price"]}")

while True:
    print_menu()
    n = int(input())
    match n:
        case 0: print("종료하겠습니다"); break
        case 1: insert_book()
        case 2: select_book()