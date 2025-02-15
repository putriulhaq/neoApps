from flask import Flask, blueprints, request
from config import DB
from flask_restx import Api
import pymysql
app = Flask(__name__)
authorizations = {
    "Bearer Auth": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}
api = Api(app, version="1.0", title="Neo APIs", description="API's Neo with Authentication", authorizations=authorizations)

try:
    conn = pymysql.connect(**DB)
    conn.ping() 
    print("Database connected successfully!")
    conn.close()
except Exception as e:
    print(f"Database connection failed: {e}")


from apis.user import api as user_ns
api.add_namespace(user_ns, path="/user")

if __name__ == "__main__":
    app.run(debug=True)