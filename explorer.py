class Explorer:
    def __init__(self):
        self.path = "/"
        self.content = list()

    def get_path(self):
        return self.path
    
    def get_content(self):
        content = ""
        for item in range(10):
            content += str(item) + "\n"

        return content
    
    def fetch_content(path):
        print("fetching")