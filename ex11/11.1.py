# a program to practice classes further

class Publication:
    def __init__(self, publication_name):
        self.publication_name = publication_name

    def get_publication_details(self):
        return f"name:{self.publication_name}"


# Book class is a subclass for Publication
class Book(Publication):
    def __init__(self, publication_name, pages, author):
        super().__init__(publication_name)
        self.pages = pages
        self.author = author
        self.list_of_books = []
        if publication_name not in self.list_of_books:
            self.list_of_books.append(publication_name)

    def get_publication_details(self):
        if self.publication_name in self.list_of_books:
            return f"name:{self.publication_name}\n" \
                   f"pages:{self.pages}\n" \
                   f"author:{self.author}\n"


# Magazine is a subclass for Publication
class Magazine(Publication):
    def __init__(self, publication_name, editor_in_chief):
        self.editor_in_chief = editor_in_chief
        super().__init__(publication_name)
        self.magazine_list = []
        if self.magazine_list not in self.magazine_list:
            self.magazine_list.append(publication_name)

    def get_publication_details(self):
        if self.publication_name in self.magazine_list:
            return f"name:{self.publication_name}\n" \
                   f"editor in chief:{self.editor_in_chief}\n"


# main program to test the classes, the publications are in Finnish language.
donald_duck = Magazine("Aku Ankka", "Aki Hyyppä")
cabin_number_six = Book("Hytti no:6", 200, "Rosa Liksom")
print(f"{donald_duck.get_publication_details()}\n"
      f"{cabin_number_six.get_publication_details()}")
