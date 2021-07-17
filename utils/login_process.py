import time
from datetime import datetime
from flask import json, jsonify
from models.account import Account
# convert  class Account -> dictionary

# 如果希望将数据导出为字典,type=1 导出为list,type=0
def Class_To_Dict(data_list, fields, type=0):
    if not type:  # 导出为数组
        user_list = []
        for u in data_list:
            temp = {}
            for f in fields:
                # if f in ['create_time','login_time']:
                #     now = datetime.now()  # current date and time
                #     temp[f]=now.strftime(getattr(u,f), "%Y-%m-%d %H:%M:%S ")
                # else:
                temp[f] = getattr(u, f)
            user_list.append(temp)
    else:
        user_list = {}
        for f in fields:
            user_list[f] = getattr(data_list, f)

    return jsonify(user_list)
# user_list[f] = Account.__getattr__(data_list,f)
# user_list[f] = data_list.__getattribute__(f)