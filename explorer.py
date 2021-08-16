class Explorer:
    def __init__(self):
        self.path = "/"
        self.content = list()

    def get_path(self):
        return self.path
    
    def get_content(self):
        test = ""
        for x in range(10):
            test += str(x) + "\n"

        return test
    
    def fetch_content(path):
        print("fetching")