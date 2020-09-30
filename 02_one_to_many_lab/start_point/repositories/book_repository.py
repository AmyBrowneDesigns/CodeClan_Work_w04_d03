from db.run_sql import run_sql
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, genre, author_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.author.id]
    result = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in books:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], row['genre'], row['id'])
        books.append(book)
    return books



# functions/methods that deal with crud data related to book table in library database