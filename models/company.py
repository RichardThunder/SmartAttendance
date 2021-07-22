from db_config import db_init as db

class Company(db.Model):
    __tablename__ = 'company'
    aid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    companyname = db.Column(db.String(255), nullable=False)
    department = db.Column(db.String(255), nullable=True)


    def __repr__(self):
        return '<Company %s, %s>' % (self.companyname, self.department)