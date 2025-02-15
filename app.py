from flask import Flask, blueprints, request
from flask_restx import Api
import pymysql
from database import get_connection
app = Flask(__name__)
authorizations = {
    "Bearer Auth": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}
api = Api(app, version="1.0", title="Neo APIs", description="API's Neo with Authentication", authorizations=authorizations)

conn = get_connection()


from apis.user import api as user_ns
api.add_namespace(user_ns, path="/user")

if __name__ == "__main__":
    app.run(debug=True)