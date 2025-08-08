#5.Create a function sum_numbers(*args) that accepts any number of numeric arguments and returns their sum.Test it with 2, 3, and 5 numbers.
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(2, 3))
print(sum_numbers(5,6,7))             
print(sum_numbers(1, 2, 3, 4, 5))    
