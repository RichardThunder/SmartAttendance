from models.company import Company
from db_config import db_init as db


class Change_company_company_Operation():
    def __init__(self):
        self.__fields__ = ['department', 'companyname']


    def _change_company_company(company, department, companyname, forcompany):
        # 数据模型类 创建对象
        user_data = Company.query.filter(Company.department == department, Company.companyname == forcompany).first()
        db.session.delete(user_data)
        db.session.commit()
        me = Company(**company)
        # 使用数据库链接对接 在对应表添加一条数据记录
        db.session.add(me)
        db.session.commit()
        data = {'code': 0, 'message': 'success'}
        return data