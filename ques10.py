#10.Given a list of temperatures in Celsius [36.5, 37.0, 39.2, 35.6, 38.7],convert them to Fahrenheit using map(),Filter out those above 100°F using filter().
celsius = [36.5, 37.0, 39.2, 35.6, 38.7]
fahrenheit = list(map(lambda c: round((c * 9/5) + 32,2), celsius))
above_100 = list(filter(lambda f: f > 100, fahrenheit))
print("Fahrenheit:", fahrenheit)
print("Above 100°F:", above_100)
