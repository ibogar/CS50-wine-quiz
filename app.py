from cs50 import SQL
from flask import flash, Flask, redirect, render_template, request, url_for
import unicodedata

app = Flask(__name__)
app.secret_key = '1ee5e1abbb938a522cfe77d6f1804c36fb8f7dabe29b9142b157edb725065ec1'

db = SQL("sqlite:///quiz.db")

def ascii_string(text):
    ascii_text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')
    return ascii_text

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        delete_question = request.form.get("selected_question")
        if delete_question:
            db.execute("DELETE FROM quiz WHERE id=?", delete_question)
            flash("Question deleted successfully!", "success") 
        else:
            flash("Please search for a question and select one of them to be deleted.", "error")  
            
        return render_template("search.html")
    return render_template("search.html")

@app.route("/search_results", methods=["GET", "POST"])
def search_results():
    if request.method == "POST":
        search_paramether = ascii_string(request.form.get("question"))
        results = db.execute("SELECT id, question, answer FROM quiz WHERE ascii_question LIKE ?", ("%" + search_paramether + "%"))
        if results:
            return render_template("search_results.html", results=results)
        
        else:
            flash("Didn't find any question, please try again.", "no results")
            return redirect("/search")
    return redirect("/search")


@app.route("/add_question", methods=["GET", "POST"])
def add_question():
    if request.method == "POST":
        question = request.form.get("question")
        ascii_question = ascii_string(question)
        answer = request.form.get("answer")
        
        if question and answer:
            db.execute("INSERT INTO quiz (question, answer, ascii_question) values (?, ?, ?)", question, answer, ascii_question)
            flash("Question added successfully!", "success")  
        else:
            flash("Please fill in both fields.", "error")  
            
        return render_template("add_question.html")
    return render_template("add_question.html")

@app.route("/")
def index():
    return redirect(url_for("home"))