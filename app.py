from flask import render_template,request,Flask
from cs50 import SQL

app = Flask(__name__)

db = SQL("mysql://root:YES@localhost:3306/cs50")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    books = db.execute("select * from book_list where title like ?","%"+ request.args.get("q") +"%")
    return render_template("search.html",books = books)