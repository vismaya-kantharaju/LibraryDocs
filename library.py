import datetime


class Book:
    """
    Represents a book in the library.
    
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        publication_year (int): The publication year of the book.
        is_lent (bool): Indicates whether the book is currently lent out or not.
    """
    
    def __init__(self, title, author, publication_year):
        """
        Initializes a Book instance.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            publication_year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_lent = False


class Library:
    """
    Represents a library containing a collection of books.
    
    Attributes:
        books (list): A list of Book objects in the library.
    """
    
    def __init__(self):
        """
        Initializes a Library instance.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book to the library.
        
        Args:
            book (Book): A Book object to be added to the library.
        """
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")
    
    def lend_book(self, title, borrower_name):
        """
        Lends a book from the library to a borrower.
        
        Args:
            title (str): The title of the book to be lent.
            borrower_name (str): The name of the person borrowing the book.
        
        Returns:
            str: A message indicating the status of the lending operation.
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_lent:
                    book.is_lent = True
                    lent_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"Book '{book.title}' lent to {borrower_name} on {lent_date}.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is currently lent out.")
                    return
        print(f"Sorry, the book '{title}' is not available in the library.")

    def view_available_books(self):
        """
        Displays the list of available books in the library.
        """
        available_books = [book for book in self.books if not book.is_lent]
        if not available_books:
            print("No books are currently available.")
        else:
            print("Available books:")
            for book in available_books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")


def main():
    """
    Main function to simulate library management operations.
    """
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Lend a book")
        print("3. View available books")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            publication_year = int(input("Enter the publication year: "))
            book = Book(title, author, publication_year)
            library.add_book(book)
        elif choice == "2":
            title = input("Enter the title of the book to lend: ")
            borrower_name = input("Enter the name of the borrower: ")
            library.lend_book(title, borrower_name)
        elif choice == "3":
            library.view_available_books()
        elif choice == "4":
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
