from flask import request, jsonify, make_response
from flask_restx import Namespace, Resource, fields, reqparse
import requests
from models.user import UserModel

api = Namespace("user", description="Users Informations")

# Swagger model 
user_model = api.model("User", {
    "email": fields.String(required=True, description="User's email"),
    "first_name": fields.String(required=True, description="User's first name"),
    "last_name": fields.String(required=True, description="User's last name"),
    "avatar": fields.String(required=True, description="User's profile image URL")
})
# user_parser = reqparse.RequestParser()

@api.route("/fetch")
class FetchUsers(Resource):
    @api.doc(description="try this if wanna using correct url: http://127.0.0.1:5000/user/fetch?page=1")
    def get(self):
        if "page" not in request.args: # if page params is missing
            return {"error": "Missing required parameter: 'page'"}, 400
        
        page = request.args.get("page", 1)  # Default page

        response = requests.get(f"https://reqres.in/api/users?page={page}")

        if response.status_code == 200:
            data = response.json()["data"]
            for user in data:
                UserModel.fetch_insert_user(user)
            return {"message": "Users fetched and saved successfully", "data": data}, 200
        return {"error": "Failed to fetch users"}, 500

@api.route("/")
class UserList(Resource):
    def get(self):
        users = UserModel.get_all_users()
        return {"users": users}, 200
    
    @api.expect(user_model)
    @api.doc(description="Add a new user")
    def post(self):
        data = request.json
        UserModel.insert_user(data)
        return {"message": "User added successfully"}, 201
    
    
@api.route("/<int:user_id>")
class UserDetail(Resource):
    def get(self, user_id):
        user = UserModel.get_user(user_id)
        if user:
            return {"user": user}, 200
        return {"error": "User not found"}, 404
    
    @api.expect(user_model)
    @api.doc(description="Updated a new user")
    def put(self, user_id):
        data = request.json
        # data['user_id'] = user_id
        UserModel.update_user(data, user_id)
        return {"message": "User updated successfully"}, 200
    
    @api.doc(security=["Bearer Auth"])
    def delete(self, user_id):
        auth = request.headers.get("Authorization")
        if auth != '3cdcnTiBsl':
            return {"error": "Unauthorized"}, 401

        # user_id = request.json
        UserModel.delete_user(user_id)
        return {"message": "User deleted successfully"}, 200 