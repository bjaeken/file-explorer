from explorer import Explorer

class Menu:
    def __init__(self):
        self.explorer = Explorer()

    def main(self):
        self.display_menu()

    def display_menu(self):
        border = 15*"==="
        print(F"""{border}\nCurrent directory: {self.explorer.get_path()}
            \rContent in directory:\n{self.explorer.get_content() + border}\n""")
        self.get_input()

    def get_input(self):
        input("Where do you want to go? ")
 
if __name__ == "__main__":
    menu = Menu()
    menu.main()