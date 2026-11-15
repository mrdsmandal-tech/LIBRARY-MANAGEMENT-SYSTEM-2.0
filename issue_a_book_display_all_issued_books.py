import json
import os

issued_books={}
with open("issued_books.json","w") as p:
    json.dump(issued_books,p,indent=4)
def issue():
    with open("all_books.json","r") as p:
        books=json.load(p)
    book=input("Enter the book id you are issuing: ")
    student=input("enter the student id: ")
    if book in books and books[book]["copies"]!=0:
        books[book]["copies"]=int(books[book]["copies"])-1
        with open("all_books.json","w") as p:
            json.dump(books,p,indent=4)
        if(os.path.exists("issued_books.json")
        and os.path.getsize("issued_books.json")!=0):
            with open("issued_books.json","r") as p:
                issued=json.load(p)
        else:
            issued={}
        issued[book]=books[book]
        with open("issued_books.json","w") as p:
            json.dump(issued,p,indent=4)
        if os.path.exists("issued_books.json") and os.path.getsize("issued_books.json")!=0:
            with open("issued_books.json","r") as p:
                record=json.load(p)
        else:
            record={}
        name=input("Enter the name of the book: ")
        name_s=input("Enter the student name: ")
        aut=input("Enter the author: ")

        issued[book]={
            "student id":student,
            "name":name,
            "student":name_s,
            "author":aut,

        }
        with open("issued_books.json","w") as p:
            json.dump(issued,p,indent=4)
        print("book issued successfully")
    else:
        print("book not found or copies aren't available")

def display_issued_books():
    with open("issued_books.json","r") as p:
      books=json.load(p)
    print(books)

