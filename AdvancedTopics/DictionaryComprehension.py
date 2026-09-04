# Python Dictionary Comprehension
# Last Updated : 18 Apr, 2026

# Dictionary comprehension is used to create a dictionary in a short and clear way. It allows keys and values to be generated from a loop in one line. This helps in building dictionaries directly without writing muanimaliple statements.
list1 = [1, 2, 3, 4, 5]
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
dic = {x:y for (x,y ) in zip(list1, names)}
print(dic)

# Using fromkeys() Method
list1 = ['a', 'b', 'c', 'd', 'e']
dic = dict.fromkeys(list1, 0)  # Initialize all keys with a default value of 0
print(dic)

# Initializing counters or scores
# You can initialize multiple items with the same starting value.

players = ["Alice", "Bob", "Charlie"]
scores = dict.fromkeys(players, 0)
print(scores)

settings_keys = ["dark_mode", "notifications", "auto_save"]
settings_values = [False, True, True]
settings = dict(zip(settings_keys, settings_values))
print(settings)

# settings = dict.fromkeys(settings_keys, False)
# print(settings)

new_set = lambda x, y: x*y
print(new_set(2, 3))

a = 'GeeksforGeeks'
upper = lambda x: x.upper()  
print(upper(a))


v = 'hello world'.upper()
print(v)

def starts_a(w):
    return w.startswith("a")

li = ["apple", "banana", "avocado", "cherry", "apricot"]
res = filter(starts_a, li)
print(list(res))

li = ["apple", "banana", "avocado", "cherry", "apricot"]

from functools import reduce

even = []
def filter_even(x):
    print(x)
    for i in x:
        print(i)
        if i % 2 == 0:
            even.append(i)
    return even
print(even)
lit = [1, 2, 3, 4, 5]
f_even = filter_even(lit)
print(f_even)
fil = filter(f_even, lit)
mp  = map(lambda x: x * 2, fil)
new_li = reduce(lambda x, y: x + y, mp)
print(new_li)

def even(lit):
    even =  []
    for i in lit:
        if i % 2 == 0:
            even.append(i)
    return even
lit = [1, 2, 3, 4, 5]
ev = even(lit)
print(ev)

Student1 = {
    "Math": 23,
    "age": 20,
}

Student2 = {
    "Math": 15,
    "age": 19,
    "major": "Physics"
}

# Student3 = {
#     "Math": 18,
#     "age": 21,
#     "major": "Physics"
# }

# students = [Student1, Student2, Student3]
default_dic = {}

for student in [Student1, Student2]:
    default_dic.update(student)
print(default_dic)

for student in [Student1, Student2]:
    # default_dic.update(student)
    for key, value in student.items():
        default_dic[key] = value
print(default_dic)

try:
    animals = ['lion', 'cat', 'lion', 'lion', 'lion', 'jaguar']
    counts = {}
    for animal in animals:
        if animal in counts:
            counts[animal] += 1
        else:
            counts[animal] = 1

    print(counts)
except:
    print(Exception('bad request'))