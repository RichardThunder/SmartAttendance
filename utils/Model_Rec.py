import zipfile

from imutils import paths
import numpy as np
import imutils
import pickle
import cv2
import os
import sys
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC


# 将根目录（execute所在目录）添加到环境变量

# 将execute文件所在目录添加到根目录
def add_path_to_sys():
    rootdir = "."
    # rootdir = os.getcwd()
    sys.path.append(rootdir)
    return rootdir


rootdir = add_path_to_sys()


def load_model():
    # 人脸检测的置信度
    confidence_default = 0.5
    # 从磁盘加载序列化面部检测器
    # proto_path = os.path.sep.join([self.detector_path, "deploy.prototxt"])
    # model_path = os.path.sep.join([self.detector_path, "res10_300x300_ssd_iter_140000.caffemodel"])
    proto_path = "./model_face_detection/deploy.prototxt"
    model_path = "./model_face_detection/res10_300x300_ssd_iter_140000.caffemodel"
    detector = cv2.dnn.readNetFromCaffe(proto_path, model_path)

    # # OpenCV深度学习人脸检测器的路径
    detector_path = "./model_face_detection"
    # # OpenCV深度学习面部嵌入模型的路径
    embedding_model = "./model_facenet/openface_nn4.small2.v1.t7"
    # # 训练模型以识别面部的路径
    recognizer_path = "./saved_weights/recognizer.pickle"
    # # 标签编码器的路径
    le_path = "./saved_weights/le.pickle"

    # 从磁盘加载序列化面嵌入模型
    embedded = cv2.dnn.readNetFromTorch(embedding_model)

    # 加载实际的人脸识别模型和标签
    recognizer = pickle.loads(open(recognizer_path, "rb").read())
    le = pickle.loads(open(le_path, "rb").read())

    # 构造人脸id的字典，以便存储检测到每个id的人脸次数，键为人名(ID)，值初始化为0，方便统计次数
    face_name_dict = dict(zip(le.classes_, len(le.classes_) * [0]))
    # 初始化循环次数，比如统计10帧中人脸的数量，取最大值进行考勤
    loop_num = 0
    # 循环来自视频文件流的帧
    while self.cap.isOpened():
        loop_num += 1
        # 从线程视频流中抓取帧
        ret, frame = self.cap.read()
        QApplication.processEvents()
        if ret:
            # 调整框架的大小以使其宽度为900像素（同时保持纵横比），然后抓取图像尺寸
            frame = imutils.resize(frame, width=900)
            (h, w) = frame.shape[:2]
            # 从图像构造一个blob, 缩放为 300 x 300 x 3 像素的图像，为了符合ResNet-SSD的输入尺寸
            # OpenCV Blog的使用可参考：https://www.pyimagesearch.com/2017/11/06/deep-learning-opencvs-blobfromimage-works/
            image_blob = cv2.dnn.blobFromImage(
                cv2.resize(frame, (300, 300)), 1.0, (300, 300),
                (104.0, 177.0, 123.0), swapRB=False, crop=False)
            # 应用OpenCV的基于深度学习的人脸检测器来定位输入图像中的人脸
            detector.setInput(image_blob)
            # 传入到ResNet-SSD以检测人脸
            detections = detector.forward()

            # 初始化一个列表，用于保存识别到的人脸
            face_names = []

            # 在检测结果中循环检测
            # 注意：这里detection为ResNet-SSD网络的输出，与阈值的设置有关，具体可以参考prototxt文件的输出层，输出shape为[1, 1, 200, 7]
            # 7 表示的含义分别为 [batch Id, class Id, confidence, left, top, right, bottom]
            # 200 表示检测到的目标数量，具体可参考SSD的论文，针对每幅图像，SSD最终会预测8000多个边界框，通过NMS过滤掉IOU小于0.45的框，剩余200个。
            for i in np.arange(0, detections.shape[2]):
                # 提取与预测相关的置信度（即概率），detections的第3维
                confidence = detections[0, 0, i, 2]

                # # 用于更新相机开关按键信息
                # if not self.cap.isOpened():
                #     self.ui.bt_open_camera.setText(u'打开相机')
                # else:
                #     self.ui.bt_open_camera.setText(u'关闭相机')

                # 过滤弱检测
                if confidence > confidence_default:
                    # 计算面部边界框的（x，y）坐标， 对应detections的4,5,6,7维（索引为3-7），含义分别代表：
                    # x_left_bottom, y_left_bottom, x_right_top, y_right_top
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    # 提取面部ROI
                    # 提取人脸的长和宽，本例中为 397 x 289
                    face = frame[startY:endY, startX:endX]
                    (fH, fW) = face.shape[:2]

                    # 确保面部宽度和高度足够大，以过滤掉小人脸(较远)，防止远处人员签到，以及过滤误检测
                    if fW < 100 or fH < 100:
                        continue

                    # 为面部ROI构造一个blob，然后通过面部嵌入模型传递blob以获得面部的128-d量化
                    # shape 为 (1, 3, 96, 96)
                    face_blob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                                                      (96, 96),  # 调整到 96 x 96 像素
                                                      (0, 0, 0), swapRB=True, crop=False)
                    # 传入到 FaceNet人脸识别模型中，将 96 x 96 x 3 的人脸图像转换为128维度的向量
                    embedded.setInput(face_blob)
                    # 128 维的向量，shape=(1, 128)
                    vec = embedded.forward()
                    # 使用SVM对人脸向量进行分类
                    # prediction 为一向量，其shape的第一个维度为人脸库中ID的数量，返回分类概率的列表
                    prediction = recognizer.predict_proba(vec)[0]
                    # 取概率最大的索引
                    j = np.argmax(prediction)
                    # 得到预测概率
                    probability = prediction[j]
                    # 通过索引j找到人名(ID)转化为one-hot编码前的真实名称，也就是人脸数据集的文件夹名称，亦即数据库中ID字段的值
                    name = le.classes_[j]

                    # 统计各人脸被检测到的次数
                    face_name_dict[name] += 1

                    # 绘制面部的边界框以及相关的概率
                    text = "{}: {:.2f}%".format(name, probability * 100)
                    # 构造人脸边界框
                    y = startY - 10 if startY - 10 > 10 else startY + 10
                    cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
                    frame = cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255),
                                        2)
                    face_names.append(name)

            # bt_liveness = self.ui.bt_blinks.text()
            # if bt_liveness == '停止检测':
            #     ChineseText = PutChineseText.put_chinese_text('./utils/microsoft.ttf')
            #     frame = ChineseText.draw_text(frame, (330, 80), ' 请眨眨眼睛 ', 25, (55, 255, 55))

            # 显示输出框架
            show_video = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
            # opencv读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage。
            # QImage(uchar * data, int width, int height, int bytesPerLine, Format format)
            self.showImage = QImage(show_video.data, show_video.shape[1], show_video.shape[0],
                                    QImage.Format_RGB888)
            self.ui.label_camera.setPixmap(QPixmap.fromImage(self.showImage))

            if loop_num == FR_LOOP_NUM:
                print(self.face_name_dict)
                print(face_names)
                # 找到10帧中检测次数最多的人脸
                # Python字典按照值的大小降序排列，并返回键值对元组
                # 第一个索引[0]表示取排序后的第一个键值对，第二个索引[0]表示取键
                most_id_in_dict = \
                    sorted(self.face_name_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)[0][0]
                # 将当前帧检测到次数最多的人脸保存到self.set_name集合中
                self.set_name = set()
                self.set_name.add(most_id_in_dict)
                # self.set_name = set(face_names)
                self.set_names = tuple(self.set_name)
                print(self.set_name, self.set_names)

                self.record_names()
                self.face_name_dict = dict(zip(le.classes_, len(le.classes_) * [0]))
                loop_num = 0
            else:
                pass
        else:
            self.cap.release()


# 训练人脸识别模型，静态方法
# @staticmethod
def train_model():
    Generator()
    TrainModel()
    print("训练完成")
    return "训练完成"


# 将根目录（execute所在目录）添加到环境变量


def Generator():
    # 人脸数据所在路径
    global embedder
    # face_data = f"{rootdir}/face_dataset"
    face_data = f"./static"
    # 输出面部嵌入的序列化数据库的路径
    embeddings = f"./saved_weights/embeddings.pickle"
    # OpenCV深度学习人脸检测器的路径
    detector_path = f"./model_face_detection/"
    # OpenCV深度学习面部嵌入模型的路径；Torch深度学习模型，可产生128-D面部嵌入
    # https://cmusatyalab.github.io/openface/models-and-accuracies/
    embedding_model = f"./model_facenet/openface_nn4.small2.v1.t7"
    # 置信度
    default_confidence = 0.5
    detector_path = "./model_face_detection"
    # 从磁盘加载序列化面部检测器
    print("[INFO] loading face detector...")
    proto_path = "./model_face_detection/deploy.prototxt"
    model_path = "./model_face_detection/res10_300x300_ssd_iter_140000.caffemodel"

    # proto_path = os.path.sep.join([detector_path, "deploy.prototxt"])
    # model_path = os.path.sep.join([detector_path, "res10_300x300_ssd_iter_140000.caffemodel"])
    print(proto_path)
    print(model_path)
    detector = cv2.dnn.readNetFromCaffe(proto_path, model_path)
    print("read complete")
    embedder = cv2.dnn.readNetFromTorch(embedding_model)
    # 人脸图像的路径
    print("[INFO] quantifying faces...")
    image_paths = list(paths.list_images(face_data))

    # 初始化提取的面部嵌入列表和相应的人名
    known_embeddings = []
    known_names = []

    # 初始化处理的人脸总数
    total = 0

    for (i, imagePath) in enumerate(image_paths):
        # 从图像路径中提取人名
        print("[INFO] processing image {}/{}".format(i + 1, len(image_paths)))
        name = imagePath.split(os.path.sep)[-2]

        # 加载图像，将其大小调整为宽度为600像素（同时保持纵横比），然后抓取图像尺寸
        image = cv2.imread(imagePath)
        image = imutils.resize(image, width=600)
        (h, w) = image.shape[:2]

        # 从图像构造一个blob
        image_blob = cv2.dnn.blobFromImage(
            cv2.resize(image, (300, 300)), 1.0, (300, 300),
            (104.0, 177.0, 123.0), swapRB=False, crop=False)

        # 应用OpenCV的基于深度学习的人脸检测器来定位输入图像中的人脸
        detector.setInput(image_blob)
        detections = detector.forward()

        # 确保至少找到一张脸
        if len(detections) > 0:
            # 假设每个图像只有一张脸，找到概率最大的边界框
            i = np.argmax(detections[0, 0, :, 2])
            confidence = detections[0, 0, i, 2]

            # 确保最大概率的检测也意味着最小概率测试（从而帮助滤除弱检测）
            if confidence > default_confidence:
                # 计算面部边界框的（x，y）坐标
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # 提取面部ROI并获取ROI维度
                face = image[startY:endY, startX:endX]
                (fH, fW) = face.shape[:2]

                # 确保面部宽度和高度足够大
                if fW < 20 or fH < 20:
                    continue

                # 为面部ROI构造一个blob，然后通过面部嵌入模型传递blob以获得面部的128-d量化
                face_blob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                                                  (96, 96), (0, 0, 0), swapRB=True, crop=False)
                embedder.setInput(face_blob)
                vec = embedder.forward()

                # 将人物名和相应的脸部嵌入添加到各自的列表中
                known_names.append(name)
                known_embeddings.append(vec.flatten())
                total += 1

    # 将面部嵌入+名称 保存到磁盘
    print("[INFO] serializing {} encodings...".format(total))
    data = {"embeddings": known_embeddings, "names": known_names}
    f = open(embeddings, "wb")
    f.write(pickle.dumps(data))
    f.close()


def TrainModel():
    # 面部嵌入的序列化db的路径
    embeddings_path = f"{rootdir}/saved_weights/embeddings.pickle"
    # 训练识别面部的输出模型的路径
    recognizer_path = f"{rootdir}/saved_weights/recognizer.pickle"
    # 输出标签编码器的路径
    le_path = f"{rootdir}/saved_weights/le.pickle"

    # 加载面嵌入
    print("[INFO] loading face embeddings...")
    data = pickle.loads(open(embeddings_path, "rb").read())

    # 编码标签
    print("[INFO] encoding labels...")
    le = LabelEncoder()
    labels = le.fit_transform(data["names"])

    # 训练用于接受人脸128-d嵌入的模型，然后产生实际的人脸识别
    print("[INFO] training model...")
    recognizer = SVC(C=1.0, kernel="linear", probability=True)
    recognizer.fit(data["embeddings"], labels)

    # 将实际的人脸识别模型写入磁盘
    f = open(recognizer_path, "wb")
    f.write(pickle.dumps(recognizer))
    f.close()

    # 将标签编码器发送到磁盘
    f = open(le_path, "wb")
    f.write(pickle.dumps(le))
    f.close()


def zip_Dir(startDir, file_news, ):
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
    for dirpath, dirnames, filenames in os.walk(startDir):
        fpath = dirpath.replace(startDir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
            print('压缩成功')
    z.close()
