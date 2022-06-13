from flask_restful import Resource, reqparse
from flask import send_file
from models.file import FileModel


class File(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('content',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="Every item needs a user_id."
                        )

    
    def get(self, name):
        file = FileModel.find_by_name(name)
        if file:
            pass
        return {'message': 'file not found'}, 404

    def post(self, name):
        if FileModel.find_by_name(name):
            return {'message': "A file with name '{}' already exists.".format(name)}, 400

        data = File.parser.parse_args()

        file = FileModel(name, **data)

        try:
            file.save_to_db()
        except:
            return {"message": "An error occurred inserting the file."}, 500

        

    
    def put(self, name):
        data = File.parser.parse_args()

        file = FileModel.find_by_name(name)

        if file:
            file.name = data['name']
        
        file.save_to_db()



class FileList(Resource):
    def get(self):
       return {'files': list(map(lambda x: x.json(), FileModel.query.all()))}