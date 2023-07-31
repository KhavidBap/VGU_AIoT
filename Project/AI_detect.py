from keras.models import load_model
import cv2
import numpy as np
import base64
from PIL import Image
import io

np.set_printoptions(suppress=True)
model = load_model("keras_Model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()
camera = cv2.VideoCapture(0)


def AI_Identify():
    def compress_image(image, quality = 25):
        temp_image = Image.fromarray(image)
        buffer = io.BytesIO()
        temp_image.save(buffer, format='JPEG', quality=quality)
        compressed_image = Image.open(buffer)
        return np.array(compressed_image)

    ret, image = camera.read()

    image = compress_image(image, quality=25)
    res, frame = cv2.imencode(".jpg", image)
    data = base64.b64encode(frame)

    image = cv2.resize(image, (224,224), interpolation=cv2.INTER_AREA)
    cv2.imshow("Webcam Image", image)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image/127.5) - 1

    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    return class_name[2::], data