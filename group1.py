from flask import Flask, request, render_template
import sqlite3

db = "group1.db"

app = Flask(__name__)
conn = sqlite3.connect(db)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS gym_membership (" \
    "id INTEGER PRIMARY KEY AUTOINCREMENT," \
    "name TEXT NOT NULL," \
    "bmi REAL," \
    "email TEXT," \
    "phone TEXT," \
    "address TEXT," \
    "start DATE," \
    "end DATE,"\
    "gender TEXT CHECK (gender IN ('M', 'F'))," \
    "disabilities TEXT" \
    ")"
)
conn.commit()
conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    bmi = request.form["bmi"]
    email = request.form["email"]
    address = request.form["address"]
    start = request.form["start"]
    end = request.form["end"]
    gender = request.form["gender"]
    disabilities = request.form["disabilities"]
    phone = request.form["phone"]
    
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO gym_membership (name, bmi, email, address, start, end, gender, disabilities, phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, bmi, email, address, start, end, gender, disabilities, phone))
    conn.commit()
    conn.close()
    return render_template("success.html")

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000, debug=True)
