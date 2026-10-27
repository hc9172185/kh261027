# 독서 종료 등록 조회 메뉴
from unittest import case

book_list = []

def print_menu():
    print("0. 종료하기")
    print("1. 독서 등록하기")
    print("2. 등록한 책 보기")

def insert_book():
    print("---- 독서를 등록하세요. ----")
    t = input()
    p = input()
    d = {
        "title" : t ,
        "price" : p
    }
    book_list.append(d)
    print("~~~ insert finish ~~~")

def select_book():
    print("---- 이 책이 등록이 되었어요. ----")
    for d in book_list:
        print(f"{d["title"]} , {d["price"]}")

while True:
    print_menu()
    n = int(input())
    match n:
        case 0: print("감사합니다~ 또 오세요!!") ;break
        case 1: insert_book()
        case 2: select_book()