# method override

class Drink:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("<Drink>self.name : ", self.name)

class Coffee(Drink):
    pass
    # def print_info(self):
    #     print("<Coffee>self.name : ", self.name)

d = Drink("딸기스무디")
c = Coffee("곡물라떼")

d.print_info()
c.print_info()