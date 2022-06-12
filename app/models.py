from . import db
from sqlalchemy.sql import func
from datetime import datetime

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Student {self.firstname}>'