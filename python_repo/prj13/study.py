# 모듈 전체 가져오기
# 접근방법 : 모듈명 이름
from person import Person
# study.person.person()
# study.person.f01
# print(study.person.(x)

# 특정 요소만 가져오기
# from person import y , f01
# from person import f01 as f04
# f04()

# def f01():pass

x = Person("hong" , 1234)
y = Person("kim" , 30)
z = Person("lee" , 40)

print(x.name)
print(x.age)