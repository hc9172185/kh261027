# 샌드위치 (빵 야채 금액)
print("")
print("---빵을 1개 고르고, 야채를 자유롭게 추가하세요")

# 빵 메뉴판
print("\n---- 빵 선택----\n")
print("1. 식빵 1000")
print("2. 호밀빵 2000")
print("3. 플렛 브레드 3000")
# 빵 선택 최종 금액
bread_num = input("빵 번호 : ")
if bread_num == "1":
    price = 1000
elif bread_num == "2":
    price = 2000
elif bread_num == "3":
    price =3000

while True:
    # 야채 메뉴판 반복문
    print("0. 야채 선택 종료")
    print("1. 올리브 1000원")
    print("2. 오이 2000원")
    print("3. 양상추 3000원")
    # 야채 선택 최종 금액
    veg_num = input("야채 번호 : ")
    if veg_num == "1":
        price = price + 1000
    elif veg_num == "2":
        price = price + 2000
    elif veg_num == "3":
        price = price + 3000
    elif veg_num =="0":
        break
    print(f"결제하실 금액은 {price} 원 입니다")
