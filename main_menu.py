from add_new_book_display_all_books import *
from delete_book import *
from issue_a_book_display_all_issued_books import *
from register_new_student import *
from return_book import *
from search_for_book import *
def main_menu():
    while True:
        print("==========LIBRARY MANAGEMENT SYSTEM============")
        print("1.Add a new book")
        print("2. Display all books")
        print("3. search for a book")
        print("4. Register new student")
        print("5. Issue a book")
        print("6. Display issued books")
        print("7. Return a book")
        print("8. Delete a book")
        print("9. Exit")
        print("=================================================")
        choice = int(input("Enter your choice(1-9): "))
        if choice == 1:
            add_new_book()
        elif choice == 2:
            display_all_books()
        elif choice == 3:
            search()
        elif choice == 4:
            register()
        elif choice == 5:
            issue()
        elif choice == 6:
            display_issued_books()
        elif choice == 7:
            Return()
        elif choice == 8:
            delete_book()
        elif choice == 9:
            print("Thank you for using this program")
            break
        else:
            print("Please enter a valid choice")

main_menu()