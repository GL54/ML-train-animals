import json
from flask import Flask, Response, request, jsonify
from io import BytesIO
import base64
from flask_cors import CORS, cross_origin
import os

import glob

from keras.models import load_model
from keras_preprocessing.image import load_img, img_to_array


from keras import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Input, Lambda, Dense, Flatten

from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
from glob import glob
import numpy as np

import pandas as pd
import seaborn as sns


from matplotlib import pyplot as plt
app = Flask(__name__)
CORS(app)
model1 = load_model('model\BC.h5', compile=False)
lab = {0: 'dog',
       1: 'horse',
       2: 'elephant',
       3: 'butterfly',
       4: 'chicken',
       5: 'cat',
       6: 'cow',
       7: 'sheep',
       8: 'spider',
       9: 'squirrel'}


def output(location):
    img = load_img(location, target_size=(224, 224, 3))
    img = img_to_array(img)
    img = img/225
    img = np.expand_dims(img, [0])
    answer = model1.predict(img)
    y_class = answer.argmax(axis=-1)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = lab[y]
    return res


@app.route("/image", methods=['GET', 'POST'])
def image():
    if (request.method == "POST"):
        file = request.files["file"]
        file.save(os.path.join('uploads', file.filename))
        data_dir = './uploads'
        image = data_dir + '/' + file.filename
        answer = output(image)
        answer = {
            "name": answer
        }
        print(answer)

        os.remove(image)

        return json.dumps(answer)
