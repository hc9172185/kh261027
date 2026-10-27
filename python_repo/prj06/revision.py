print("")
print("햄버거 1개 고르고, 서브 메뉴 1개 고르고, 음료 선택하세요")

print("---햄버거 선택---")
print("1. 치즈버거 4000원")
print("2. 불고기버거 5000원")
print("3. 새우버거 5000원")

burger_num = input()
if burger_num == "1":
    price = 4000
elif burger_num == "2":
    price = 5000
elif burger_num == "3":
    price = 5000

while True:
    print("---사이드 메뉴 선택---")
    print("1. 감자튀김 3000원")
    print("2. 모짜렐라 치즈스틱 3000원")
    print("3. 맥너겟 4000원")
    print("4. 사이드 메뉴 선택 안함")

    side_num = input()
    if side_num == "1":
        price += 3000
    elif side_num == "2":
        price += 3000
    elif side_num == "3":
        price += 4000
    elif side_num == "4":
        break

print("---음료 선택---")
print("1. 콜라 2000원")
print("2. 제로 콜라 3000원")
print("3. 사이다 2000원")

drink_num = input()
if drink_num =="1":
    price += 2000
elif drink_num =="2":
    price += 3000
elif drink_num == "3":
    price += 2000


print(f"결제하실 금액은 {price} 원 입니다")

