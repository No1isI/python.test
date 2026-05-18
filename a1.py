class Library():
    def __init__(self,title,author,avalibility):
        self.title=title
        self.author=author
        self.avalibility=avalibility 
    def display(self):
        print(self.title)
        print(self.author)
        print(self.avalibility)

class Book(Library):
    def __init__(self, author,title,avalibility,borrowed):
        self    