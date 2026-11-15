import json
def search():
       a=input("enter the book id you want to search: ")
       with open('all_books.json','r') as f:
           all_books = json.load(f)
       if a in all_books:

           print("found the book",all_books[a])
       else:
           print("book not found")




