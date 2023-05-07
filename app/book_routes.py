from app import db
from app.models.book import Book
from .route_helpers import validate_model
from flask import Blueprint, jsonify, make_response, request, abort

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST"])

def create_book():
    request_body = request.get_json()
    new_book = Book.from_dict(request_body)

    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)

@books_bp.route("", methods=["GET"])
def get_all_books():

    title_query = request.args.get("title")
    
    if title_query:
        books = Book.query.filter_by(title=title_query)
    else:
        books = Book.query.all()
    
    books_list = []
    
    for book in books:
        books_list.append(book.make_book_dict())
    return jsonify(books_list), 200


@books_bp.route("/<id>", methods=["GET"])
def get_one_book(id):
    book = validate_model(cls, id)
    return book.make_book_dict(), 200

    
@books_bp.route("/<id>", methods=["PUT"])
def update_book(id):
    book = validate_model(cls, id)
    
    request_body = request.get_json()
    
    if request_body.get("title") is None or request_body.get("description") is None:
        return make_response({"message":"something is missing"}, 400)

    book.title= request_body["title"]
    book.description = request_body["description"]
    
    db.session.commit()
    
    return make_response(f"Book #{book.id} successfully updated")
    

@books_bp.route("/<id>", methods=["DELETE"])
def delete_book(id):
    book = validate_model(cls, id)

    db.session.delete(book)
    db.session.commit()

    return make_response(f"Book #{book.id} successfully deleted")