import pymysql
from database import get_connection

class UserModel:
    @staticmethod
    def fetch_insert_user(user):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            try:
                print('test')
                cursor.execute("""
                    INSERT IGNORE INTO users (id, email, first_name, last_name, avatar, created_at)
                    VALUES (%s, %s, %s, %s, %s, NOW())
                """, (user["id"], user["email"], user["first_name"], user["last_name"], user["avatar"]))
                conn.commit()
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def insert_user(user):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            try:
                print('test')
                cursor.execute("""
                    INSERT INTO users (email, first_name, last_name, avatar, created_at)
                    VALUES (%s, %s, %s, %s, NOW())
                """, (user["email"], user["first_name"], user["last_name"], user["avatar"]))
                conn.commit()
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def get_user(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, email, first_name, last_name, avatar FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    @staticmethod
    def get_all_users():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, email, first_name, last_name, avatar FROM users")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users
    
    @staticmethod
    def update_user(user, id):
        print(user)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE users SET email=%s, first_name=%s, last_name=%s, avatar=%s, updated_at=NOW() WHERE id=%s
        """, (user["email"], user["first_name"], user["last_name"], user["avatar"], id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete_user(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        cursor.close()
        conn.close()