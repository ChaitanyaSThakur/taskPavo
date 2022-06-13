from flask_restful import Resource,reqparse
from models.user import UserModel
from db import db
import os

work_dir=os.getcwd() + '/users/'

class UserRegister(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument('folderpath',
        type=str,
        required=False
    )
   
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message":"A user with that username already exists"}

        user_folder = os.path.join(work_dir, data['username'])
        os.mkdir(user_folder)
        user= UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201
