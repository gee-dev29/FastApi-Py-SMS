try:
    animals = ['jaguar', 'cat', 'lion', 'lion', 'lion', 'jaguar']
    counts = {}
    for animal in animals:
        if animal in counts:
            counts[animal] += 1
        else:
            counts[animal] = 1

    print(counts)

    from functools import reduce
    def Reduce(numbers):
        for num in numbers:
            print(num)
        reduce(numbers)

    nb = [2,4,6,7]
    red = Reduce(nb)

    print(red)
except:
    print(Exception('bad request'))


s = [1, 2, 3, 4, 'ajoke']
res = map(str, s)
print(list(res))

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1)

print(factorial(5))