import pymysql
from pymysql.cursors import DictCursor
from config import DB

def get_connection():
    try:
        conn = pymysql.connect(**DB, cursorclass=DictCursor)
        print(f"Database connection successfully")
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None
