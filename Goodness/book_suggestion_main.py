def main_menu():
    books = ["The Hobbit", "The Mystery", "Brave kind"]
    choice = 0

    while True:
        print("Welcome to the book suggestion system!")
        print("1. Get Suggestions")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Update Book")
        print("5. Show all Books")
        print("6. Exit")

        books_choice = int(input("Enter your choice: "))

        if books_choice == 1:
            book, page = suggest_books(books)
            print("Book for the day: ")
            print("Book Title: ", book)
            print("Page: ", page)

        elif books_choice == 2:
            book_name = input("Enter the book name: ")
            result = add_book(books, book_name)
            
            if result:
                print("Book has been added successfully!")
            else:
                print("This Book already exists!")

        elif books_choice == 3:
            book_name = input("Enter the book name to remove: ")
            result = remove_book(books, book_name)
        
        if result:
            print("Book has been removed successfully!")
        else:
            print("Book is not found!")

        elif books_choice == 4:
            old_book_name = input("Enter the old book name: ")
            new_book_name = input("Enter the new book name: ")
            result = update_book(books, old_book_name, new_book_name)

            if result:
                print("Book updated successfully!")
            else:
                print("Book cannot be found!")

        elif books_choice == 5:
            books = show_all_books(books)
            print("All Books:")
            for book in books:
                print(book)

        elif books_choice == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid option")

main_menu()


