import json
import os

new="all_students.json"
def load():
    if os.path.exists(new):
        with open(new, "r") as k:
            try:
                return json.load(k)
            except json.JSONDecodeError:
                return {}
    else:
        return {}
def save(all_students):
    with open(new, "w") as k:
        json.dump(all_students, k, indent=4)

def register():
  data=load()
  a = input("enter student id: ")
  if a in data:
     print("student already registered")
     return

  b = input("enter student name: ")
  c = input("enter student branch: ")
  d = input("enter student semester: ")
  data[a] = {
            "name": b,
            "branch": c,
            "semester": d
        }
  save(data)
  print("student registered")







