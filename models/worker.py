from db_config import db_init as db


class Worker(db.Model):
    __tablename__ = 'worker'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(255), nullable=True)
    department = db.Column(db.String(255), nullable=True)
    contact = db.Column(db.String(255), nullable=True)
    company = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return '<worker %s, %s>' % (self.id, self.name)
