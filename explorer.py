from item import Item
from pathlib import Path

class Explorer:
    def __init__(self):
        self.path = "/home/pi/Pictures"
        self.lib = Path(self.path)
        self.content = list()
        self.fetch_content()

    def get_path(self):
        return self.path
    
    def get_content(self):
        items = ""
        if len(self.content) > 0:
            for item in self.content:
                items += item.__str__()
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
           
