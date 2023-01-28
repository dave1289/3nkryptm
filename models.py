from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
   db.app = app
   db.init_app(app)

class User(db.Model):
   """blogly users"""
   __tablename__ = 'users'

   @classmethod
   def get_by_id(cls, id):
      return cls.query.filter_by(id=id).one()

   def __repr__(self):
      p = self
      return f'<USER id={p.user_id} first_name={p.first_name} last_name={p.last_name} image_url={p.img_url}>'

   user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   user_name = db.Column(db.Text, nullable=False)
   conversations = db.Column(db.Integer, nullable=False)
