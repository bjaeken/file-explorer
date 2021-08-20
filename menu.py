from explorer import Explorer

class Menu:
    def __init__(self):
        self.explorer = Explorer()
        self.exit = False
        self.commands = {}

    def main(self):
        self.fill_commands()
        while not self.exit:
            self.display_menu()

    def fill_commands(self):
        self.commands = {
            "!": "To exit the program.",
            "/": "To go to the parent directory.",
            "directory": "To navigate to typed directory."
        }
 
    def display_menu(self):
        border = 15*"==="
        print(F'''{border}\nCurrent directory: {self.explorer.get_path()}
            \rContent in directory:\n{self.explorer.get_content()}
            \r{self.display_commands() + border}\n''')
        self.get_input()

    def display_commands(self):
        command_list = ""
        for command, desc in self.commands.items():
            command_list += F"Com: {command}, desc: {desc}\n"
        
        return command_list

    def get_input(self):
        loc = input("Where do you want to go? ")
        if loc == "!" or loc == "":
            self.exit = True
        else:
            self.explorer.set_path(loc)
 
if __name__ == "__main__":
    menu = Menu()
    menu.main()