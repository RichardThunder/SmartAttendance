import datetime
from Back.db_config import db_init as db
from sqlalchemy import DateTime
class attendance(db.Model):
    __tablename__='attendance'
    recordNum=db.Column(db.Integer, primary_key=True,autoincrement=True)
    id=db.Column(db.Integer, nullable=False)
    CkInTime = db.Column(db.DateTime, nullable=False,default=datetime.datetime.now())
    CkOutTime= db.Column(db.DateTime, nullable=False,default=datetime.datetime.now())

    def __repr__(self):
        return '<attendance %s, %s>' % (self.recordNum, self.id)

