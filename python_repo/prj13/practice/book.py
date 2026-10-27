class book:
    def __init__(self ,name , price):
        self.name = name
        self.price = price

    def __str__(self):
        return(f"도서이름: {self.name} , 도서가격: {self.price}")