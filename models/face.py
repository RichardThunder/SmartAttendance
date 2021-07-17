from db_config import db_init as db


class Face(db.Model):
    __tablename__='face'
    fid=db.Column(db.Integer, primary_key=True,autoincrement=True)
    FacePath=db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<face %s, %s>' % (self.recordNum, self.id)

