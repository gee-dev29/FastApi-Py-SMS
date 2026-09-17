
def generate_numbers(n):
    for number in range(1, n):
        yield number
print(next(generate_numbers(50)))

# for num in genNum:
#     print(next(num))

def get_scores():
    for i in range(1_000_000):
        yield i
scores = get_scores()
# print(scores)
print(next(scores))
print(next(scores))