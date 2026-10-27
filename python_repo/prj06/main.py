# up down
import random

answer = random.randint(1,50)

while True:
    x = int(input("1~50 사이에 숫자를 입력하세요"))

    if answer > x:
        print("up")
    elif answer < x:
        print("down")
    else :
        print("correct")
        break
