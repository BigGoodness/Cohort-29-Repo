import random
books = ["The Hobbit", "The Mystery", "Brave kind"]

def suggest_books(books):
    another = "yes"

    random_book = random.randChoice(books)
    random_page = random.randint(1, 100)

    print("Book for the day:")
    print("Book Title:", random_book)
    print("Page:", random_page)

    Would you like another suggestion (yes/no):


def add_book(books):
    book_name = input("Enter the book name: ")

    if book_name is in books:
        print("Book already exists")
    else:
        books.append(book_name)
        print("Book added")


def remove_book(books):
    book_name =input("Enter the book name: ")

    if book_name is in books:
        book_name.remove(books)
        print("Book removed")
    else:
        print("Book not found")


def update_book(books):

    old_book_name = input("Enter the name of the old book: ")
    new_book_name = input("Enter the name of the new book: ")

    if old_book_name is in books:
        old_book_name.update(new_book_name)
        print("Book updated")
    else:
        print("Book not found")


def show_all_books(books):
    for each book in books:
        print("book")
