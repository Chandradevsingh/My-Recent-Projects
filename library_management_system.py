class library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"These are all the available books in our library : {self.name}")
        for book in self.bookslist:
            print(book)

    def lendBook(self, user):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender_Book database has been updated. You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, user, book):
        self.bookslist.append(book)
        print("Book has been added to the book list")

    def return_book(self, book):
        self.booksList.remove(book)

if __name__ == '__main__':
    library = library(['Java', 'Python', 'C++', 'C'], 'Dev Library')

    while(True):
        print(f"Welome to the {library.name}")
        print("1. Display Books")
        print("2. Lend a Book")        
        print("3. Add a Book")        
        print("4. Return a Book")
        user_choice = int(input())
        if user_choice == 1:
            library.displayBooks()

        elif user_choice ==  2:
            book = input("Enter the name of the book you want to lend : ")
            user = input("Enter your name : ")
            library.lendDict[book] = user

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add : ")
            user = input("Enter your name : ")
            library.addBook(book, user)

        elif user_choice == 4:    
            book = input("Enter the name of the book you want to return : ")
            library.return_book(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2 != "c" and user_choice2 != "q"):
            user_choice == input("Enter your choice : ")
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue