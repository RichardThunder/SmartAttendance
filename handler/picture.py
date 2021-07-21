import os
import zipfile

from flask import Blueprint, request, Response, jsonify, json, make_response, send_from_directory
from api.picture_api import *
from utils.Model_Rec import *
# picture 蓝图
picture = Blueprint('picture', __name__)


# 创建 picture/upload 路由 处理图片上传
@picture.route("/train", methods=["GET"])
def train():
    data = train_model()
    startdir = "./saved_weights"  # 要压缩的文件夹路径
    file_news = startdir + '.zip'  # 压缩后文件夹的名字
    zip_Dir(startdir,file_news)
    response = make_response(
        send_from_directory(".", "saved_weights.zip", as_attachment=True))
    return response
############train##############
# GET 方法, 训练完成后返回权重文件 并压缩.saved_weight.zip
# 需要接受并解压,得到三个权重与标签文件, 放至 ./saved_weights 文件夹下
###############################

@picture.route("/detect",methods=["POST","GET"])
def detect():

    f = request.files['file']
        # base_path = os.path.dirname(__file__)
        # filepath = os.path.join(os.path.split(base_path)[0], 'static', f.filename.split('_')[0])
        # filepath = os.path.join('.\static', f.filename.split('_')[0])
        # if not os.path.exists(filepath):
        #     os.makedirs(filepath)
        #     Face_Operation.path_insert(int(f.filename.split('_')[0]), filepath)
        # all_files = os.listdir(filepath)
        # num = 0
        # for each_file in all_files:
        #     num = num + 1
        # str_path = str(num) + '.' + f.filename.split('.')[1]
        # upload_path = os.path.join(filepath, Path(str_path))
    f.save("./1.jpg")

    return load_model(f)