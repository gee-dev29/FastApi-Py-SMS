# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."

# calculation =  +,-,*, /
# comparison = >, <, ==, !=, >=, <=, ===, !==
# combination = and, or, not
# age = 17
# has_licence = False
# name = "Shola"
# # AND - both must be true
# can_drive = age >= 18 and has_licence
# print(f"Can {name} drive? {can_drive}")
# can_drive_or_not = age >= 18 or has_licence
# print(f"Can {name} drive or not? {can_drive_or_not}")

#  Nested if-else statements

# has_ticket = True
# age = 13
# if has_ticket:
#     if age >= 18:
#         print("You can enter the concert.")
#     else:
#         print("You are too young to enter the concert.")
# else:    print("You need a ticket to enter the concert.")

# numbers = [1,5,7,8,9]
# list1 = [var **2 for var in numbers]
# print(list1)
# evenNumber = []
# oddNumber = []
# for item in numbers:
#     if item % 2 == 0:
#         evenNumber.append(item)
#     else:
#         oddNumber.append(item) 
# if len(evenNumber) == 0:
#     print('there are no even numbers')
# else:
#     print('these are the even numbers: ', evenNumber)
# if len(oddNumber) == 0:
#     print('there are no even numbers')
# else:
#     print('these are the even numbers: ', oddNumber)



# for list2Item in list2:
#     print('these are the items in the: ',  list2Item)
# # print('these are the items in the: ',  list2) 

# print(1%2)
# name  = "Shola"
# num = int(name)
# print(num)

# apple_store = {"banana": 4,"apple": 10,"orange": 2,"pear": 3}

# print(apple_store['banana'])

# list1 = ['cat', 'dog', 'fish', 'fish', 'dog']

# count = 0
# for item in list1:
#   if item == 'fish':
#     count = count + 1
# print(count)

# import random

# foundNumber = []
# # duplicateNumber = []
# while len(foundNumber) < 10:
#     randNumber = random.randint(1, 10)
#     if randNumber not in foundNumber:
#         foundNumber.append(randNumber)
#     else:
#       foundNumber.append(randNumber)
#       # print('This number is already in the list: ', randNumber)
# print(foundNumber)
# print('These are the duplicate numbers: ', foundNumber)

students = {
        "John": {
            "age": 20,
            "score": 85
        },
        "Mary": {
            "age": 21,
            "score": 92
        },
        "Peter": {
            "age": 19,
            "score": 100
        }
}
# score = {}
# for student in students:
#     score[student] = students[student]["score"]
#     # print(list(score.values()))
# for key, value in score.items():
#     if value > 85:
#         print(f"The highest scoring student is: {key} with a score: {value}")
# print(list(score.values()))
# name = input("Enter student name: ")
# age = int(input("Enter student age: "))
# score = int(input("Enter student score: "))

# students[name] = {"age": age, "score": score}
# print(f"Student {name} added successfully!")
# print(students)

with open("./csv/sample-1mb.csv", "a") as file2:
    name = input("Enter Your name: ")
    file2.write(f"name: {name}\n")
    age = input("Enter age : ")
    file2.write(f"age: {age}\n")
with open("./csv/sample-1mb.csv", "r") as file2:
    reader = csv.reader(file2)
    for row in reader:
        print(row)

file = open("./csv/sample-1mb.csv", "r")

file.close()
# import csv
# import json
# list = []
# with open("./csv/sample-1mb.csv", "r") as file:
#     # current = csv.DictReader(file)
#     current= {}
#     for line in file:
#         key, value = line.strip().split(": ")
#         current[key] = value
#         if key != "name" and key != "age":
#             list.append(current)

#         if key == "age":
#             current["age"] = int(current["age"])
#             list.append(current)
#             current = {}
# print(json.dumps(list))

# from pathlib import Path
# file_path = Path("csv")
# data_folder = file_path / "data" / "sample-1mb.csv"
# mkdir = data_folder.mkdir(parents=True, exist_ok=True)
# print(file_path.is_dir())
# print(mkdir.absolute())
# with open("./csv/sample-10kb.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         row['Name'] = "Emma"
#         print(row)


import csv
list = []
with open('./exercise/files/data/sample-1mb.csv','r') as file:
    data = csv.DictReader(file)
    print(data)
    dict = {}
    for row in file:
        key, value = row.strip().split(": ")
        dict[key] = value
        if key != "name" and key != "age":
            list.append(dict)

        if key == "age":
            dict["age"] = int(dict["age"])
            list.append(dict)
            dict = {}

print(list)

try:
    numbers = [1, 2, 3, 4, 5]
    index = 10 
    print(numbers[index])
except IndexError as e:
    print(f"IndexError: {e}")