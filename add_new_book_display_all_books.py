import json
import os
add="all_books.json"
def load():
    if os.path.exists(add):
        with open(add, "r") as k:
            try:
                return json.load(k)
            except json.JSONDecodeError:
                return {}
    else:
        return {}
def save(all_books):
    with open(add, "w") as k:
        json.dump(all_books, k, indent=4)
def add_new_book():
    data=load()
    while True:
        try:
            a=int(input("enter book id: "))
            break
        except ValueError:
            print("enter a valid book id")
    b=input("enter new book title: ")
    c=input("enter book's author name: ")
    d=input("enter books category: ")
    e=input("enter available copies: ")
    data[a]={
        "title":b,
        "author":c,
        "category":d,
        "copies":e
    }
    save(data)
    print("book added successfully")



def display_all_books():
    try:
        with open("all_books.json", "r") as r:
            print(json.dumps(json.load(r),indent=4))
    except FileNotFoundError:
        print("file not found")

