import os
from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.getenv("SAMTIK_DB_HOST", "localhost")
DB_PORT = os.getenv("SAMTIK_DB_PORT", "5433")
DB_NAME = os.getenv("SAMTIK_DB_NAME", "samtik_db")
DB_USER = os.getenv("SAMTIK_DB_USER", "samtik_admin")
DB_PASS = os.getenv("SAMTIK_DB_PASS", "Davich0214781")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
