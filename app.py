from flask import Flask
from flask_restful import Api

from db import db
from resources.user import UserRegister
from resources.file import File, FileList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(UserRegister, '/user') 
api.add_resource(File, '/user/file/<string:name>')
api.add_resource(FileList, '/user/files/')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)