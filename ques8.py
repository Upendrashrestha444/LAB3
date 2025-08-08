#8.Given a list of numbers [1, 2, 3, 4, 5], use map() and a lambda function to return a new list with each number doubled.
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))

print(doubled)
