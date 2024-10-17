from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    rating: Mapped[float]

with app.app_context():
    db.create_all()



with app.app_context():
    new_book = Books(id=2, title="Harry Potter", author="J.K", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

all_books = []

@app.route('/')
def home():
    return render_template("index.html", books = all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        new_book = {
        "title":request.form["title"],
        "author":request.form["author"],
        "rating":request.form["rating"]
        }
        all_books.append(new_book)
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

