from flask_restful import Resource,reqparse
from models.user import UserModel
from db import db
import os

work_dir=os.getcwd() + '/users/'

class UserRegister(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument('uid',
        type=int,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument('folderpath',
        type=str,
        required=False
    )
    parser.add_argument('filename',
        type=str,
        required=False
    )
    parser.add_argument('content',
        type=str,
        required=False
    )
    
   
    def post(self):
        data = UserRegister.parser.parse_args()
        # user = UserModel(self)
        # print(user)
        if UserModel.find_by_username(data['username']):
            return {"message":"A user with that username already exists"}

        user_folder = os.path.join(work_dir, data['username'])
        os.mkdir(user_folder)
        data['folderpath']=user_folder
        user= UserModel(**data)
        user.save_to_db()
        return {"message": "User created successfully"}, 201


class UserFile(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('uid',
        type=int,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument('filename',
        type=str,
        required=False
    )
    parser.add_argument('content',
        type=str,
        required=False
    )

    def get(self, name):
        file = UserModel.find_by_name(name)
        if file:
            pass
        return {'message': 'file not found'}, 404

    def post(self):

        # data = UserFile.parser.parse_args()

        # file = UserModel(name, **data)
        # data=UserModel.fetch_user(id)
        # user= UserModel(**data2)
        # user_folder = os.path.join(work_dir, str(data['username']))
        # result = self.query.with_entities(self.col1,self.col2,self.col3)
        # print(result)

        # filepath= os.path.join(work_dir + '/x' + data2.username + '/')
        # os.chdir(filepath)
        # userid=file.user_id
        # print(userid)
        data = UserRegister.parser.parse_args()
        # user = UserModel(self)
        # print(user)
        if UserModel.find_by_filename(data['filename']):
            return {"message":"A file with that filename already exists"}

        
        
        db.session.query(UserModel).filter(UserModel.uid==data['uid']).update({
            UserModel.filename : data['filename'], UserModel.content: data['content']
        })

        db.session.commit()
        # print(UserModel.filename)
        # os.chdir(str(UserModel.folderpath))
        user_folder = os.path.join(work_dir, data['username'])
        os.chdir(user_folder)
        with open(data['filename'], mode="a") as file:
            file.write(data['content'])
        


        # data = UserFile.parser.parse_args()
        
        # # print(os.getcwd())
        
        # if UserModel.find_by_filename(self.filename):
        #     return {'message': "A file with name '{}' already exists.".format(self.filename)}, 400

        # data = UserFile.parser.parse_args()

        # file = UserModel(name, **data)

        # try:
        #     file.save_to_db()
        # except:
        #     return {"message": "An error occurred inserting the file."}, 500

class ListFiles(Resource):    
    def listfilesforuser(name):
        pass


