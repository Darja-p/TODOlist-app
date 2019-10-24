from . import db
import datetime


class TODOS(db.Model):
    """Data model for books"""

    __tablename__ = 'todos'
    id = db.Column(db.Integer,
                   primary_key=True)
    description = db.Column(db.String(150),
                         index=False,
                         unique=True,
                         nullable=False)
    due_date = db.Column(db.DateTime, default=(datetime.datetime.now() + datetime.timedelta(days=1)))


    @staticmethod
    def from_dict(dict):
        return TODOS(description=dict['description'],due_date = dict['due_date'])

    def to_dict(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'description': self.description,
           'due_date'   : self.due_date,
       }