from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    author_id= db.Column(db.Integer, db.ForeignKey('author.id'))
    author= db.relationship("Author", back_populates="books")

    @classmethod
    def from_dict(cls, book_data):
        new_book = Book(title=book_data["title"], description=book_data["description"])
        return new_book
    
    def make_book_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            description=self.description,
            
        )
    