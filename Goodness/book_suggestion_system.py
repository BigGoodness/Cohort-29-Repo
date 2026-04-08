import random
books = ["The Hobbit", "The Mystery", "Brave kind"]

def suggest_books(books):
    another = "yes"

    while another == 'yes':
        random_book = random.choice(books)
        random_page = random.randint(1, 100)

        return random_book, random_page


def add_book(books, book_name):
    if book_name in books:
        books.append(book_name)
        return True


def remove_book(books, book_name):
    if book_name in books:
        books.remove(book_name)
        return True
    return False

def update_book(books, old_book_name, new_book_name):
    if old_book_name in books:
        index = books.index(old_book_name)
        books[index] = new_book_name
        return True
    return False


def show_all_books(books):
    return books
