# In app.py
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
DATABASE = "database.db"

# Create the database and table (if they don't exist)
def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create the my_table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Insert some sample data (you can customize this)
    cursor.execute("INSERT INTO my_table (name, email) VALUES (?, ?)", ("John Doe", "john@example.com"))
    cursor.execute("INSERT INTO my_table (name, email) VALUES (?, ?)", ("Jane Smith", "jane@example.com"))

    conn.commit()
    conn.close()

@app.route("/")
def index():
    # Create the database and table (if needed)
    create_database()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM my_table")
    data = cursor.fetchall()
    conn.close()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
