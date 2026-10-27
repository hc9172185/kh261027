import random as randum
from pokemon.pokemon import Pokemon

def process_attack(attacker,defender):
    print(f"{attacker.name}의 공격!")
    dmg = attacker.atk - defender.arm
    defender.hp = dmg
    print(f"데미지 : {dmg} ")
    print(f"{defender}의 남은 체력 : {defender.hp}")
    if defender.hp <= 0:
        print(f"배틀 종료, {attacker.name} WIN!")
        return True
    else:
        return False

print("=== POKEMON ===")

p1 = Pokemon("리자몽", 100, 100, 50)
p2 = Pokemon("거북왕", 100, 100, 50)
p3 = Pokemon("이상해꽃", 100, 100, 50)

pokemons = [p1, p2, p3]

n =input("선택할 포켓몬 번호 : ")
match n:
    case "1": user = p1 = Pokemon("리자몽", 100, 100, 50)
    case "2": user = p2 = Pokemon("거북왕", 100, 100, 50)
    case "3": user = p3 = Pokemon("이상해꽃", 100, 100, 50)
    case _ : user = None

r = randum.randint(1, 3)
match r:
    case 1: com = p1 = Pokemon("리자몽", 100, 100, 50)
    case 2: com = p2 = Pokemon("거북왕", 100, 100, 50)
    case 3: com = p3 = Pokemon("이상해꽃", 100, 100, 50)
    case _ :com = None

print(f"user : {user}")
print(f"com : {com}")

# battle

while True:
    # user -> com
    is_finish = process_attack(user, com)
    if is_finish: break

    # com -> user
    is_finish = process_attack(com, user)
    if is_finish: break