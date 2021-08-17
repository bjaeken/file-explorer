class Item:
    def __init__(self, name, is_directory, size):
        self.name = name
        self.is_directory = is_directory
        self.size = size
    
    def __str__(self):
        return f'{self.name} - {"directory" if self.is_directory else "file"} - size {self.size}'