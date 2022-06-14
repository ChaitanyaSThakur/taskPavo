from db import db
from sqlalchemy.sql import select


class UserModel(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    folderpath = db.Column(db.String(200))
    filename= db.Column(db.String(80))
    content = db.Column(db.String(400))
    
    

    def __init__(self, uid, username, folderpath, filename, content):
        self.uid = uid
        self.username = username
        self.folderpath = folderpath
        self.filename = filename
        self.content = content
    
    def json(self):
        return {'uid': self.uid,'name': self.name, 'folderpath': self.folderpath, 'filename': self.filename, 'content': self.content}

        

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # def update_db(self,id,name,text):
    #     x = db.session.query(self).get(id)
    #     x.filename=name
    #     x.content=text
    #     db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(uid=_id).first()

    @classmethod
    def find_by_filename(cls, filename):
        return cls.query.filter_by(filename=filename).first()

    
    