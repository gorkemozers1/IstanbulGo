import sqlite3 as sql

def connect():
    conn = sql.connect("data/museum.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM muzeler")
    muzeler = cur.fetchall
