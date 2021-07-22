from models.worker import Worker
from db_config import db_init as db


class delete_worker_Operation():

    def _delete_worker(id):
        # 数据模型类 创建对象
        user_data = Worker.query.filter(Worker.id == id).first()
        db.session.delete(user_data)
        db.session.commit()
        data = {'code': 0, 'message': 'success'}
        return data