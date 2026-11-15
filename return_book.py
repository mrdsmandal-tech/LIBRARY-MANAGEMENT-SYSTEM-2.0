
import json


def Return():
    with open("all_books.json", "r") as f:
        data = json.load(f)
    with open("all_students.json", "r") as j:
        students = json.load(j)
    try:
        with open("issued_books.json", "r") as f:
            issued = json.load(f)
    except:
        issued = {}

    book = input("enter book id: ")
    student = input("enter student id: ")

    if (
        book in issued
        and issued[book]["student id"] == student
        and student in students
        and book in data
    ):

        data[book]["copies"] = int(data[book]["copies"]) + 1
        with open("all_books.json", "w") as f:
            json.dump(data, f, indent=4)

        issued.pop(book)
        with open("issued_books.json", "w") as f:
            json.dump(issued, f, indent=4)

        print("book is returned")
    else:
        print("wrong book id or student id")
