from book import Book

with open("books.txt") as file:
    for line in file:
        books = line.strip().split(",")
        print(books)

books[0].get_title()

