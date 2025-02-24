from fastapi import FastAPI
from app.core.config import DB_URL

print(DB_URL)  # Должно вывести значение DB_URL

app = FastAPI()

@app.get("/")
def read_root():
    return {"db_url": DB_URL}