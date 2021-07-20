# from flask import Blueprint, request, Response, jsonify, json
# from api.picture_api import *
# # picture 蓝图
# picture = Blueprint('picture', __name__)
#
# #创建 picture/upload 路由 处理图片上传
# @picture.route("/upload",methods=["POST"])
# def upload():
#     data=Picture_upload()
#     return jsonify(data)
#
# @picture.route("/train",methods=["REQUEST"])
# def train():
#     data=Picture_train()
#     return jsonify(data)
#
#
