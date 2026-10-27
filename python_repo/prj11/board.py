# 게시판

board_list =[]

def insert_board():
    print("---- 게시물 작성 ----")
    t = input("제목을 입력해주세요.")
    c = input("목록을 입력해주세요.")
    d = {
        "title" : t,
        "content" : c
    }
    board_list.append(d)
    print("게시물 작성 완료!")

def select_board():
    print("---- 게시물 목록 조회 ----")
    for x in board_list:
        print(x["title"] , "/", x["content"])

def print_menu():
    print("---- BOARD ----")
    print("0. 종료하기")
    print("1. 게시물 작성")
    print("2. 게시물 목록 조회")
    n = int(input("메뉴 변호 : "))
    return n

while True:
    n = print_menu()
    if n == 0:
        break
    match n:
        case 0:
            print("게시물 관리 프로그램 종료!")
            break
        case 1:
            insert_board()
        case 2:
            select_board()