from db_config import db_init as db
from werkzeug.security import generate_password_hash, check_password_hash


class Account(db.Model):
    __tablename__ = 'account'
    aid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pwd = db.Column(db.String(255), nullable=False)
    Identity = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<account %s, %s>' % (self.recordNum, self.id)

    def set_password(self, password):
        self.pwd = generate_password_hash(password)  # 将生成的密码保持到对应字段

    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.pwd, password)  # 返回布尔值
