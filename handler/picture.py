import os
import zipfile

from flask import Blueprint, request, Response, jsonify, json, make_response, send_from_directory
from api.picture_api import *
from utils.Model_Rec import train_model
from utils.Model_Rec import zip_Dir
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
