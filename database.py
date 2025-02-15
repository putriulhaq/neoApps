import pymysql
from pymysql.cursors import DictCursor
from dotenv import load_dotenv
import os

load_dotenv()
DB = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}
def get_connection():
    try:
        conn = pymysql.connect(**DB, cursorclass=DictCursor)
        print(f"Database connection successfully")
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None
