#9.Given a list [10, 15, 20, 25, 30], use filter() and a lambda function to extract numbers divisible by 10.
nums = [10, 15, 20, 25, 30]
divisible_by_10 = list(filter(lambda x: x % 10 == 0, nums))
print(divisible_by_10)
