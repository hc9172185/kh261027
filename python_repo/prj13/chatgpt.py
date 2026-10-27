class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + "가 멍멍!")

dog1 = Dog("슈퍼")

dog1.bark()