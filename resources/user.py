from flask_restful import Resource,reqparse
from models.user import UserModel
from db import db
import os

work_dir=os.getcwd() + '/users/'
files= []

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

        
        
        db.session.query(UserModel).filter(UserModel.username==data['username']).update({
            UserModel.filename : data['filename'], UserModel.content: data['content']
        })

        db.session.commit()
        # print(UserModel.filename)
        # os.chdir(str(UserModel.folderpath))
        user_folder = os.path.join(work_dir, data['username'])
        os.chdir(user_folder)
        with open(data['filename'], mode="a") as file:
            file.write(data['content'])
        print(os.listdir(user_folder))

        file= {'username': data['username'], 'filename': data['filename']}
        files.append(file)
        


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
    def post(self):
        data = UserRegister.parser.parse_args()
        user_folder = os.path.join(work_dir, data['username'])
        # print(os.listdir(user_folder))
        # return  os.listdir(user_folder)

        # print("Files and directories in a specified path:")
        # for filename in os.listdir(user_folder):
        #         f = os.path.join(user_folder,filename)
        #         if os.path.isfile(f):
        #             print(f)
        # directory_list = os.listdir(user_folder)
        # print("Files and directories in  current working directory :") 
        return{'message': "files in directory {}".format(os.listdir(user_folder))}

class ReadFile(Resource):
    def post(self):
        data = UserRegister.parser.parse_args()
        user_folder = os.path.join(work_dir, data['username'])
        file_path = os.path.join(user_folder, data['filename'])
        fd = os.open(file_path,os.O_RDWR)
        # fd = os.read(file_path, int(n))
        # content=os.
        return{'file content': "{}".format(os.read(fd,400))}
