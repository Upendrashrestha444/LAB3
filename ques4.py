#4.Write a function book_info(title, author, year) that prints book details.Call the function using keyword arguments in different orders.
def book_info(title, author, year):
    print(f"Title: {title}, Author: {author}, Year: {year}")

book_info(title="1984", author="George Orwell", year=1949)
book_info(year=2000, title="The Alchemist", author="Paulo Coelho")
