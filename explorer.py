class Explorer:
    def __init__(self):
        self.path = "/"
        self.content = list()

    def get_path(self):
        return self.path
    
    def get_content(self):
        return self.content
    
    def fetch_content(path):
        print("fetching")