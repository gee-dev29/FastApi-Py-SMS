numbers = [1,5,7,8,9]

squares = [x**2 for x in numbers ]
print(squares)

# Syntax

#     [expression for item in iterable if condition]

# Parameters:

#     expression: operation or value to include in the new list.
#     item: current element from the iterable.
#     iterable: sequence like a list, tuple or range.
#     if condition (optional): filter to include only items that satisfy the condition.

# with condition
numbers = [1,5,7,'8',9]
squares = [x**2 for x in numbers if isinstance(x, int)]
print(squares)

datas = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age':15},
    {'name': 'Charlie', 'age': 35}
]
newData = [data['age'] for data in datas if data['age'] < 30]
for data in newData:
  print('Ages less than 30: ', data)
# print(data)

  mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  newList = []
  rowLenght = 0
  for row in mat:
    rowLenght = len(row)
    for val in row:
      newList.append(val)
  print(newList)
  print("row length: ", rowLenght)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)

# For Loop vs List Comprehension
# For Loop	List Comprehension
# Uses multiple lines of code	Uses a single line of code
# Requires manual appending of elements	Creates the list directly
# Better for complex logic and conditions	Better for simple and concise operations
# More readable for long operations	More compact and faster to write