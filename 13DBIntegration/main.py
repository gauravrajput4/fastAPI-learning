from fastapi import FastAPI
import sqlite3

app = FastAPI()

conn=sqlite3.connect("test.db",check_same_thread=False)
cursor=conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY,
    title TEXT,
    completed BOOLEAN
    )
    """
)

conn.commit()

@app.get("/")
def home():
    return {
        "message":"SQLITE Database Integration with FastAPI"
    }