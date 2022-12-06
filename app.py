from flask import render_template,request,Flask,jsonify # as we will use json format
from cs50 import SQL

app = Flask(__name__)

db = SQL("mysql://root:YES@localhost:3306/cs50")

@app.route("/")
def index():
    # we will change the template , which can interact with user's inputs
    return render_template("api_index.html")
    # return render_template("index.html")

@app.route("/search")
def search():
    # as we will use API , we need to add condition to check whether user has typed something or not
    q = request.args.get("q")
    if q:   # if there is search 
        books = db.execute("select * from book_list where title like ?","%"+ q +"%")
    else:
        books = []
    return jsonify(books)       
    # we will return the books list with json format
    # return render_template("search.html",books = books)
    # search.html will not be used for json format as we can return the data with json