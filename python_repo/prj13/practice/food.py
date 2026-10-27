class Food:
    def __init__(self , name , price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"음식이름={self.name} , 음식가격={self.price}"