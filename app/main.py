from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

@app.get("/")
def root():
    return {"message": "Dockerized FastAPI is running 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db")
def db_test():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return {"db_response": result[0]}
