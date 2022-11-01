class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"Book: {self.name}\nAuthor: {self.author}\nPage Count: {self.page_count}\n")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"Magazine: {self.name}\nChief Editor: {self.chief_editor}\n")


publications = []
publications.append(Magazine("Donald Duck", "Aki Hyyppä"))
publications.append(Book("Compartment No. 6", "Rosa Liksom", 192))

for publication in publications:
    publication.print_information()