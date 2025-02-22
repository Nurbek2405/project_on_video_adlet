import os

from dotenv import load_dotenv

load_dotenv()



DB_URL = os.getenv("DB_URL")

print(f"{DB_URL}")