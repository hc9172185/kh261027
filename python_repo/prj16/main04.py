class coffee:
    shop = "파이썬 카페"

    def __init__(self, name):
        self.name = name

a = coffee("아메리카노")
b = coffee("라떼")

coffee.shop = "판다스 카페"

print(a.shop)
print(b.shop)