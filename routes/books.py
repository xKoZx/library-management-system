from flask import Blueprint, request, jsonify
from models import Book
from database import db

book_routes = Blueprint('book_routes', __name__)

@book_routes.route('/', methods=['GET'])
def get_books():
    title = request.args.get('title')
    author = request.args.get('author')
    books_query = Book.query
    if title:
        books_query = books_query.filter(Book.title.contains(title))
    if author:
        books_query = books_query.filter(Book.author.contains(author))
    books = books_query.all()
    return jsonify([{"id": book.id, "title": book.title, "author": book.author, "genre": book.genre, "available": book.available} for book in books])

@book_routes.route('/', methods=['POST'])
def add_book():
    data = request.json
    book = Book(title=data['title'], author=data['author'], genre=data['genre'], available=data.get('available', True))
    db.session.add(book)
    db.session.commit()
    return jsonify({"message": "Book added successfully"}), 201

@book_routes.route('/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.json
    book = Book.query.get(id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.genre = data.get('genre', book.genre)
    book.available = data.get('available', book.available)
    db.session.commit()
    return jsonify({"message": "Book updated successfully"})

@book_routes.route('/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"})