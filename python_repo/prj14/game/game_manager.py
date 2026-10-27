class GameManager:
    def start_updown_game(self):
        print("==== UP DOWN ====")

    def start_baseball_game(self):
        print("==== BASE BALL ====")

    def print_menu(self):
        print("0. exit")
        print("1. updown game")
        print("2 baseball game")

    def game_start(self):
        while True:
            self.print_menu()
            n = input("menu : ")
            match n:
                case "0":
                    print("exit");break
                case "1":
                    self.start_updown_game()
                case "2":
                    self.start_baseball_game()
                case _:
                    print("invalid option")