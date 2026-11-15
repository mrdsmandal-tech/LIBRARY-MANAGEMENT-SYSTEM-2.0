import json

def delete_book():
    enter=input("Enter the book id you want to delete: ")
    with open("all_books.json", "r") as p:
        books=json.load(p)
    if  enter in books:
        books.pop(enter)
        with open("all_books.json","w") as p:
            json.dump(books,p,indent=4)
        print("Book has been deleted")
    else:
        print("Book not found")


