from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect("staff.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user_staff (" \
"id INTEGER PRIMARY KEY," \
"staff_name TEXT," \
"password TEXT)")
conn.commit()
conn.close()

@app.route("/")
def index():
    return render_template("form-details.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    password = request.form["password"]
    conn = sqlite3.connect("staff.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_staff (staff_name, password) VALUES (?, ?)", (name, password))
    conn.commit()
    conn.close()
    return "Data submitted successfully"

if __name__ == "__main__":
    app.run(debug=True)
