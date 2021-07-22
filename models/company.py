from db_config import db_init as db

class Company(db.Model):
    __tablename__ = 'company'
    companyname = db.Column(db.String(255), primary_key=True)
    department = db.Column(db.String(255), nullable=True)


    def __repr__(self):
        return '<Company %s, %s>' % (self.companyname, self.department)