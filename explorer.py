from item import Item
from pathlib import Path

class Explorer:
    def __init__(self):
        self.path = "/"
        self.lib = Path(self.path)
        self.content = list()
        self.fetch_content()

    def get_path(self):
        return self.path

    def set_path(self, new_path):
        if new_path == "/":
            self.path = self.path[:-(self.path[::-1].find('/') + 1)]
        else:    
            self.path += F"/{new_path}"

        self.lib = Path(self.path)
        self.fetch_content()
    
    def get_content(self):
        items = ""
        if len(self.content) > 0:
            for item in self.content:
                items += str(item)
        else:
            items += "- This folder is empty\n"

        return items
    
    def fetch_content(self):
        self.content.clear()
    
        if self.lib.is_dir():
            for item in self.lib.glob("*"):
                if self.check_hidden_item(item):
                    if item.is_dir():
                        self.content.append(Item(item.name, True, item.stat().st_size))
                    else:
                        self.content.append(Item(item.name, False, item.stat().st_size))

    def check_hidden_item(self, item):
        return (not item.name.startswith("."))
           
