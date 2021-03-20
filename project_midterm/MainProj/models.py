from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

class info(db.Model):
    ab_id = db.Column(db.Integer(), primary_key=True)
    ab_name  = db.Column(db.String())
    ab_pic = db.Column(db.String())