from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from repositories.book_repository as book_repository
import repositories.author_repository as author_repository

tasks_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books/new", methods=['GET'])
def books():
    books =  book_repository.select_all()
    return render_template("books/index.html", all_books = books)
