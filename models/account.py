from db_config import db_init as db


class account(db.Model):
    __tablename__='account'
    aid=db.Column(db.Integer, primary_key=True,autoincrement=True)
    pwd=db.Column(db.String(255), nullable=False)
    Identity=db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<account %s, %s>' % (self.recordNum, self.id)

