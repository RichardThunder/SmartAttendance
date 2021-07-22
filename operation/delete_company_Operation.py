from models.company import Company
from db_config import db_init as db


class delete_company_Operation():

    def _delete_company(department, companyname):
        # 数据模型类 创建对象
        user_data = Company.query.filter(Company.department == department, Company.companyname == companyname).first()
        db.session.delete(user_data)
        db.session.commit()
        data = {'code': 0, 'message': 'success'}
        return data