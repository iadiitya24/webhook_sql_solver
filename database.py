import sqlite3

def init_db(db_name="app.db"):
    with sqlite3.connect(db_name) as conn:
        with open("data.sql", "r") as f:
            conn.executescript(f.read())